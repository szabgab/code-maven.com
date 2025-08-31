---
title: "The importance of using HTTPS"
timestamp: 2019-01-23T22:30:01
tags:
  - curl
  - tcpdump
  - httpbin
  - TLS
  - SSL
published: true
author: szabgab
archive: true
---


When browsing the Internet in the privacy of your computer it is easy to forget that it is not just you, the computer and the web site on the other end. There are other organizations on the way and there can be other people who might watch your data traffic. Demonstrating how your data can be easily recorded can make a good case for anyone to look for the little lock in the address bar of their browsers.

It can also get more web site owners to switch to https. After all it is quite easy to do it today using the free service of [Let's encrypt](https://letsencrypt.org/).


## What is HTTPS ?

In a nutshell, HTTP is the [Hypertext Transfer Protocol](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol) used by browsers to communicate with web servers.

TLS is [Transport Layer Security](https://en.wikipedia.org/wiki/Transport_Layer_Security) the new name of Secure Sockets Layer (SSL). It provides secure connection between two computers.

HTTPS is [HTTP over Transport Layer Security [TLS]](https://en.wikipedia.org/wiki/HTTPS).

## Our tools

For our demonstration we are going to use [httpbin over http](http://httpbin.org/) and [httpbin over https](https://httpbin.org/). A great service that can be used by anyone who wants to experiment with web client.

We are also going to use [curl](https://curl.haxx.se/) that makes it easy to access a web site from the command line. You could achieve the same results using your favorite browser.

Last, but not least, we are going to use [tcpdump](http://www.tcpdump.org/).
If you'd like to try this at home and you only have MS Windows, then you might want to use
[WinDump](https://www.winpcap.org/windump/) or [WireShark](https://www.wireshark.org/).

## GET over HTTP

Let's start with a simple GET request over HTTP.

```
curl 'http://httpbin.org/get?username=foobar&password=secret'
```

The response will be

```
{
  "args": {
    "password": "secret",
    "username": "foobar"
  },
  "headers": {
    "Accept": "*/*",
    "Connection": "close",
    "Host": "httpbin.org",
    "User-Agent": "curl/7.54.0"
  },
  "origin": "37.26.149.149",
  "url": "http://httpbin.org/get?username=foobar&password=secret"
}
```

You could do the same in your browser. Just visit [this url](http://httpbin.org/get?username=foobar&password=secret).

Then run the following command on your Linux/Unix machine in one terminal: You might need to install the `tcpdump` command first and you will be asked for your password as this command needs root access.

```
sudo tcpdump -vv host httpbin.org
```

This will start printing out all the communication to and from the httpbin.org server.

Then run the curl command again or visit [this url](http://httpbin.org/get?username=foobar&password=secret).

```
curl 'http://httpbin.org/get?username=foobar&password=secret'
```

In the window where you ran the command you'll see the output you are expected. That's not the interesting part.

In the window where you ran the `tcpdump` command you'll see some cryptic messages, but you will also see the following:

```
    air.65327 > ec2-23-21-245-33.compute-1.amazonaws.com.http: Flags [P.], cksum 0x7bea (correct), seq 1:111, ack 1, win 4120, options [nop,nop,TS val 1989702306 ecr 686226205], length 110: HTTP, length: 110
    GET /get?username=foobar&password=secret HTTP/1.1
    Host: httpbin.org
    User-Agent: curl/7.54.0
    Accept: */*
```

There you go. Your password was recorded as it passed through the network.

You will also see the response sent back by the server in clear text that in our case happens to contain the password again, though in regular service that should not happen. The point though is that both what you sent and what you received could be recorded by someone who listens in on the wire or on the wireless.

Not only that, but the content of the parameters can be seen in the address-bar of your browser. They will be also recorded in the log of the web server.

## POST over HTTP

POST requests seem to be more secure. For one, the data is not sent in the URL, so people watching over your shoulder cannot see it. Normally it does not get recored in the web server logs either. Though that could be changed by the web site owner.

We can tell `curl` to send a POST request instead of the default GET using the `-X` flag and then we can supply the data using the `-d` flag:

```
curl -X POST -d 'username=foobar&password=secret' 'http://httpbin.org/post'
```

This is the same when you have an HTML form using "POST" as the method of submission. Like in the next form that will open a new tab or new window:

<form method="POST" action="http://httpbin.org/post" target="_new">
<input name="username" value="foobar">
<input name="password" type="password" value="secret">
<input type="submit" value="Send">
</form>

In Firefox when you click on the submit button you'll get a pop-up warning you:

<img src="/img/firefox-http-warning.png" alt="Firefox Security warning">

On the terminal where you ran `tcpdump` you'll see, among some other output, the following:

```
    192.168.1.101.50593 > ec2-54-243-175-5.compute-1.amazonaws.com.http: Flags [P.], cksum 0xc8e5 (correct), seq 1:549, ack 1, win 4096, options [nop,nop,TS val 2187521457 ecr 795639310], length 548: HTTP, length: 548
    POST /post HTTP/1.1
    Host: httpbin.org
    User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:56.0) Gecko/20100101 Firefox/56.0
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
    Accept-Language: en-US,en;q=0.5
    Accept-Encoding: gzip, deflate
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 31
    Cookie: _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _gauges_unique_hour=1; _gauges_unique_day=1
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1

    username=foobar&password=secret[!http]
```

There, the list line is the data I've submitted via the browser.

So even though in POST requests the data cannot be seen in the address-bar of the browser, it is still sent as clear text behind the scene. So someone monitoring your traffic can still see it.


## GET over HTTPS

Let's see what happens with the same requests going over HTTPS.

```
curl 'https://httpbin.org/get?username=foobar&password=secret'
```

Or click on [this link](https://httpbin.org/get?username=foobar&password=secret).

If you look at the terminal with the `tcpdump` in it you will only see unreadable data. That's because everything is encrypted. <b>We can still see with which computer do you communicate</b>, but we cannot see the content of your request. Not even the URL you accessed.

Someone standing behind the shoulder still can see the parameters in the address-bar and it still gets recorded in the log file, but at least others cannot see all the details of your communication.

## POST over HTTPS

The same with POST requests, except the address-bar and the log files.

```
curl -X POST -d 'username=foobar&password=secret' 'https://httpbin.org/post'
```

<form method="POST" action="https://httpbin.org/post" target="_new">
<input name="username" value="foobar">
<input name="password" type="password" value="secret">
<input type="submit" value="Send">
</form>


## TL;DR

As a web site owner check out [Let's encrypt](https://letsencrypt.org/). They provide HTTPS certificates free of charge. With a little effort you can make your site and your users more secure.


