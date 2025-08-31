---
title: "Generating a self-signed cert with openssl for multiple hostnames with Subject Alternative Name"
timestamp: 2017-01-01T07:30:01
tags:
  - openssl
published: false
author: szabgab
archive: true
---


I have spent way to much time looking for solution for this problem. I've found several recommended solution, but for some
reason none of those worked for me. Finally I cobbld together this one.


First I had to create a configuration file listing the hostname in the "[ alt_names ]" section.

{% include file="examples/san.cnf" %}

Then I ran the following command:

```
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -config san.cnf -extensions san
```

Finally I configured nginx and restarted it.

To check the results, open one of the URLs in Chrome. Open the Developer Tools (hidden behind the 3 dot-menu or in the View/Developer menu item).
There you'll see if you still get the <b>Subject Alternative Name</b> error.

{% include file="examples/nginx_with_ssl.conf" %}

## Java error reporting

<b>Error making web req: IO Exception caught: java.security.cert.CertificateException: No subject alternative names present</b>

<b>req: IO Exception caught: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to
requested target</b>


