---
title: "Serving web pages over IPv6 and IPv4 and verifying it"
timestamp: 2019-05-05T17:30:01
tags:
  - IPv6. IPv4
  - curl
  - nginx
  - ping
  - ping4
  - ping6
published: true
author: szabgab
archive: true
---


Much slower than expected but [IPv6](https://en.wikipedia.org/wiki/IPv6) seems to be gaining ground. I don't
have any general statistics, but all of the VPS hosting companies I work with support IPv6 and even at homes networks I
have encountered IPv6.

So on the network layer many of my users have IPv6 enabled, and my servers also have it, but how can I make sure the web
server also serves both IPv4 and IPv6?


I'll start with the verification as you will also need to do that both before you make changes - to see what are the
problems - and after you make changes - to see if you have managed to fix them.

## IPv6 on the network

```
$ ping6 code-maven.com

PING code-maven.com(s7.hostlocal.com (2600:3c00::f03c:91ff:fedf:456f)) 56 data bytes
64 bytes from s7.hostlocal.com (2600:3c00::f03c:91ff:fedf:456f): icmp_seq=1 ttl=54 time=265 ms
64 bytes from s7.hostlocal.com (2600:3c00::f03c:91ff:fedf:456f): icmp_seq=2 ttl=54 time=286 ms
...
```

```
$ ping4 code-maven.com

PING code-maven.com (173.255.196.65) 56(84) bytes of data.
64 bytes from s7 (173.255.196.65): icmp_seq=1 ttl=45 time=312 ms
64 bytes from s7 (173.255.196.65): icmp_seq=2 ttl=45 time=238 ms
...
```


## Verify HTTP and HTTPs over IPv4 and IPv6

[curl](https://curl.haxx.se/) allows us to send http request. It has a `-I` flag that tells it to only
display the header we get. There is also a `-4` flag that tells it to use IPv4 and a `-6` flag that makes
it use IPv6.

So here is how I can check the site:

First I make sure that the request to http will redirect to the corresponding https page when using IPv4:

```
$ curl -I -4 http://code-maven.com/

HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 05 May 2019 15:44:47 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://code-maven.com/
```

Then verify the same over Ipv6:

```
$ curl -I -6 http://code-maven.com/

HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 05 May 2019 15:48:09 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://code-maven.com/
```

I can check the redirection for the www.code-maven.com hostname as well.

Then I can verify if the https version serves the page. First over IPv4 and then over IPv6.
In each case I can use `-I` to see the header or leave out the `-I` and see the actual html
content returned.

```
$ curl -I -4 https://code-maven.com/

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 05 May 2019 15:49:24 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 11559
Connection: keep-alive
```

```
$ curl -I -6 https://code-maven.com/

HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 05 May 2019 15:51:39 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 11510
Connection: keep-alive
```

## Wrong configuration

Before I fixed this domain I had results like this:

```
$ curl -I -4 http://code-maven.com/

HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 05 May 2019 15:44:47 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://code-maven.com/
```

```
$ curl -I -6 http://code-maven.com/

HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Sun, 05 May 2019 15:48:09 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: http://hostlocal.com/
```

That is, the http version over IPv4 redirected to the right place
while http over IPv6 redirected to a different site. (That was the default site on the specific server.)


## How to configure Nginx to serve over both Ipv4 and IPv6

I am using an old version of Ubuntu and thus an old version of Nginx. I think the defaults have changed since then and
you might not need all this configuration, but as far as I understand explicitly configuring this won't cause
problems even in newer versions of nginx.


Tell each <b>https</b> `server` section in your Nginx configuration to work on both IPv6 (the first row) and on IPv4 (second row):

```
  listen    [::]:443 ssl;
  listen    443 ssl;
```

Tell each <b>http</b> `server` section in your Nginx configuration to work on both IPv6 (the first row) and on IPv4 (second row):

```
  listen     [::]:80;
  listen     80;
```


Once you made the changes, reload nginx, and verify with `curl`.



