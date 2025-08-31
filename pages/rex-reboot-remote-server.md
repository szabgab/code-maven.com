---
title: "Reboot remote server with Rexify"
timestamp: 2021-04-11T09:30:01
tags:
  - Rex
  - Rexify
  - reboot
published: true
books:
  - rex
author: szabgab
archive: true
show_related: true
---


This code is based on what was discussed in [Rex Automation part 3](/rex-automation-3), it allows you to reboot a server.


{% include file="examples/rex/reboot/Rexfile" %}

Assuming you have a host with IP address 104.236.89.4 where you can login as user <b>root</b>,
this is the command you need to run:

```
rex -H 104.236.89.4 -u root reboot
```

The output will look similar to this:

```
[2021-04-11 09:18:59] INFO - Running task reboot on 104.236.89.4
The authenticity of host '104.236.89.4 (104.236.89.4)' can't be established.
ECDSA key fingerprint is SHA256:+z26G29adbKkq2iEuF07QEw9lrVG7U3r7oJrUnLMj7I.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
[2021-04-11 09:19:07] INFO - uptime before
[104.236.89.4]>	 06:19:07 up 2 min,  0 users,  load average: 0.35, 0.35, 0.15
[2021-04-11 09:19:08] INFO - Waiting for shutdown...
Connection to 104.236.89.4 closed by remote host.
[2021-04-11 09:19:09] INFO - Waiting for SSH to come back...
[2021-04-11 09:19:24] INFO - uptime after
[104.236.89.4]>	 06:19:25 up 0 min,  0 users,  load average: 1.33, 0.28, 0.09
[2021-04-11 09:19:24] INFO - All tasks successful on all hosts
```

First I had to verify the ECDSA key fingerprint of the server because this was the first time I actually accessed this machine.

It showed the current uptime (2 min), yes I just started this server for the demo.

Then the reboot and then showing that the uptime is now 0 min.

## Comments

Original [gist for reboot](https://gist.github.com/ferki/be63ad18b6b93352f2829cf691335938) that we used
before starting the pair development session.

I personally think this, or an improved version of the reboot function should be inlcuded in the standard Rex distribution.


