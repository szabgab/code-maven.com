---
title: "Exercise: Send plain text e-mail"
timestamp: 2015-11-07T09:40:01
tags:
  - exercises
  - projects
published: true
books:
  - ruby
  - python
  - javascript
  - php
author: szabgab
archive: true
---


Exercise: Send plain text e-mail.


Create a function that will get one or more addresses where `To` send the message,
0 or more address to `Cc` the message. A single addres to pretend as the `From` field.

Get a string to be the `Subject` line and some plain text to be the body of the e-mail.


By default this should assume to be running on a Linux/Unix system with a properly configured sendmail program
and use that as the underlying transporting system.


Then also add an optional parameter `SMTP` that holds the name or IP address of an
[SMTP server](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol).
When this parameter is given, use the SMTP server to send the e-mail.

