"""Test for certbot_apache.configurator for CentOS 6 overrides"""
import os
import unittest

import mock

from certbot_apache import obj
from certbot_apache import override_centos
from certbot_apache import parser
from certbot_apache.tests import util

def get_vh_truth(temp_dir, config_name):
    """Return the ground truth for the specified directory."""
    prefix = os.path.join(
        temp_dir, config_name, "httpd/conf.d")

    aug_pre = "/files" + prefix
    vh_truth = [
        obj.VirtualHost(
            os.path.join(prefix, "test.example.com.conf"),
            os.path.join(aug_pre, "test.example.com.conf/VirtualHost"),
            set([obj.Addr.fromstring("*:80")]),
            False, True, "test.example.com"),
        obj.VirtualHost(
            os.path.join(prefix, "ssl.conf"),
            os.path.join(aug_pre, "ssl.conf/VirtualHost"),
            set([obj.Addr.fromstring("_default_:443")]),
            True, True, None)
    ]
    return vh_truth

class CentOS6Tests(util.ApacheTest):
    """Tests for CentOS 6"""

    _multiprocess_can_split_ = True

    def setUp(self):  # pylint: disable=arguments-differ
        test_dir = "centos6_apache/apache"
        config_root = "centos6_apache/apache/httpd"
        vhost_root = "centos6_apache/apache/httpd/conf.d"
        super(CentOS6Tests, self).setUp(test_dir=test_dir,
                                        config_root=config_root,
                                        vhost_root=vhost_root)

        self.config = util.get_apache_configurator(
            self.config_path, self.vhost_path, self.config_dir, self.work_dir,
            version=(2, 2, 15), os_info="centos")
        self.vh_truth = get_vh_truth(
            self.temp_dir, "centos6_apache/apache")

    def test_get_parser(self):
        self.assertTrue(isinstance(self.config.parser,
                                   override_centos.CentOSParser))

    def test_get_virtual_hosts(self):
        """Make sure all vhosts are being properly found."""
        vhs = self.config.get_virtual_hosts()
        self.assertEqual(len(vhs), 2)
        found = 0

        for vhost in vhs:
            for centos_truth in self.vh_truth:
                if vhost == centos_truth:
                    found += 1
                    break
            else:
                raise Exception("Missed: %s" % vhost)  # pragma: no cover
        self.assertEqual(found, 2)

    def test_loadmod_default(self):
        ssl_loadmods = self.config.parser.find_dir(
            "LoadModule", "ssl_module", exclude=False)
        self.assertEqual(len(ssl_loadmods), 1)
        # Make sure the LoadModule ssl_module is in ssl.conf (default)
        self.assertTrue("ssl.conf" in ssl_loadmods[0])
        # ...and that it's not inside of <IfModule>
        self.assertFalse("IfModule" in ssl_loadmods[0])

        # Get the example vhost
        self.config.assoc["test.example.com"] = self.vh_truth[0]
        self.config.deploy_cert(
            "random.demo", "example/cert.pem", "example/key.pem",
            "example/cert_chain.pem", "example/fullchain.pem")
        self.config.save()

        post_loadmods = self.config.parser.find_dir(
            "LoadModule", "ssl_module", exclude=False)

        # We should now have LoadModule ssl_module in root conf and ssl.conf
        self.assertEqual(len(post_loadmods), 2)
        for lm in post_loadmods:
            arguments = self.config.parser.get_all_args(lm[:-7])
            self.assertEqual(arguments, ["ssl_module", "modules/mod_ssl.so"])
            # ...and both of them should be wrapped in <IfModule !mod_ssl.c>
            # lm[:-17] strips off /directive/arg[1] from the path.
            ifmod_args = self.config.parser.get_all_args(lm[:-17])
            self.assertEqual(ifmod_args, ["!mod_ssl.c"])

    def test_loadmod_rootconf_exists(self):
        sslmod_args = ["ssl_module", "modules/mod_ssl.so"]
        rootconf_ifmod = self.config.parser.get_ifmod(
            parser.get_aug_path(self.config.parser.loc["default"]),
            "!mod_ssl.c", beginning=True)
        self.config.parser.add_dir(rootconf_ifmod[:-1], "LoadModule", sslmod_args)
        self.config.save()
        # Get the example vhost
        self.config.assoc["test.example.com"] = self.vh_truth[0]
        self.config.deploy_cert(
            "random.demo", "example/cert.pem", "example/key.pem",
            "example/cert_chain.pem", "example/fullchain.pem")
        self.config.save()

        root_loadmods = self.config.parser.find_dir(
            "LoadModule", "ssl_module",
            start=parser.get_aug_path(self.config.parser.loc["default"]),
            exclude=False)

        mods = [lm for lm in root_loadmods if self.config.parser.loc["default"] in lm]

        self.assertEqual(len(mods), 1)
        # [:-7] removes "args[#]" from the path
        self.assertEqual(
            self.config.parser.get_all_args(mods[0][:-7]),
            sslmod_args)

    def test_loadmod_non_duplicate(self):
        # the modules/mod_ssl.so exists in ssl.conf
        sslmod_args = ["ssl_module", "modules/mod_somethingelse.so"]
        rootconf_ifmod = self.config.parser.get_ifmod(
            parser.get_aug_path(self.config.parser.loc["default"]),
            "!mod_ssl.c", beginning=True)
        self.config.parser.add_dir(rootconf_ifmod[:-1], "LoadModule", sslmod_args)
        self.config.save()
        self.config.assoc["test.example.com"] = self.vh_truth[0]
        pre_matches = self.config.parser.find_dir("LoadModule",
                                                  "ssl_module", exclude=False)
        with mock.patch("certbot_apache.override_centos.logger.info") as mock_log:
            self.config.deploy_cert(
                "random.demo", "example/cert.pem", "example/key.pem",
                "example/cert_chain.pem", "example/fullchain.pem")
            self.assertTrue(mock_log.called)
            self.assertTrue("Multiple different LoadModule" in mock_log.call_args[0][0])

        post_matches = self.config.parser.find_dir("LoadModule",
                                                   "ssl_module", exclude=False)
        # Make sure that none was changed
        self.assertEqual(pre_matches, post_matches)

    def test_loadmod_not_found(self):
        # Remove all existing LoadModule ssl_module... directives
        orig_loadmods = self.config.parser.find_dir("LoadModule",
                                                    "ssl_module",
                                                    exclude=False)
        for mod in orig_loadmods:
            noarg_path = mod.rpartition("/")[0]
            self.config.aug.remove(noarg_path)
        self.config.save()
        # get_all_args() is called for each LoadModule that was found
        getall = "certbot_apache.override_centos.CentOSParser.get_all_args"
        with mock.patch(getall) as mock_getall:
            self.config.deploy_cert(
                "random.demo", "example/cert.pem", "example/key.pem",
                "example/cert_chain.pem", "example/fullchain.pem")
            self.assertFalse(mock_getall.called)


if __name__ == "__main__":
    unittest.main()  # pragma: no cover
