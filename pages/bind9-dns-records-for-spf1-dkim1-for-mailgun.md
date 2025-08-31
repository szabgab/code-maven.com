---
title: "Bind9 DNS records for SPF1 and DKIM1 for a domain used by mailgun"
timestamp: 2019-04-09T07:30:01
tags:
  - bind
  - dns
  - mailgun
published: true
author: szabgab
archive: true
---


If you'd like to use [Mailgun](https://mailgun.com/) you will need to configure a domain or at least a hostname in a
domain that will be used to send out the messages.

You'll need to tell the world using [SPF1](https://en.wikipedia.org/wiki/Sender_Policy_Framework) and
[DKIM1](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) records that the IP addresses of Mailgun
are approved to send out messages of your domain.

This will increase the likelihood of your messages arriving to their destinations and not flagged out by SPAM filters.


They have instructions for various
[DNS providers](https://documentation.mailgun.com/en/latest/quickstart-sending.html), but
I have not seen instructions for plain old Bind9 files and it took me a while to figure them out,
but now here they are:

{% include file="examples/mailgun-domain.txt" %}

In this case I registered the <b>mg</b> hostname as in mg.hostocal.com.

## Verify your configuration

There is a [detailed explanation](https://help.mailgun.com/hc/en-us/articles/360011565514) by Mailgun.

Here are the commands I used (on a Linux system):

```
dig -t MX mg.hostlocal.com

dig -t TXT mg.hostlocal.com

dig -t TXT mx._domainkey.mg.hostlocal.com
```

