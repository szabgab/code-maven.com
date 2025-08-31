---
title: "Jenkins Pipeline: Send e-mail notifications"
timestamp: 2018-08-21T20:30:01
tags:
  - emailext
  - BuildUser
published: true
books:
  - jenkins
author: szabgab
archive: true
---


Configuring Jenkins to send e-mail will be covered later. For now let's see a few snippets of pipeline code that will send the e-mail.


{% include file="examples/jenkins/emailtext.gvy" %}


## BuildUser plugin and e-mail

{% include file="examples/jenkins/notify.gvy" %}

