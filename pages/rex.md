---
title: "Rex - (R)?ex - Rexify"
timestamp: 2021-03-23T09:30:01
tags:
  - Rex
description: "Rex (aka Rexify) is a framework allowing you to automate the configuration and maintenance of many servers"
published: true
author: szabgab
archive: true
show_related: true
---


[Rex (aka Rexify)](https://www.rexify.org/) is a framework allowing you to automate the configuration and maintenance of many servers.


* [Learn automation using (R)?ex](/automation-with-rex)
* [Multiple OS-es using (R)?ex](/rex-multiple-oses)
* [Rex Automation part 3](/rex-automation-3)
* [Setting up ELK using (R)?ex](/elk-with-rex)

Rex articles:

* [Execute Rex commands locally](/rex-run-code-locally)
* [Reboot remote server using Rex](/rex-reboot-remote-server)

<!--
   <li><a href=""></a></li>
-->

## Further Plans
* Mention the idea of separating code and data (e.g. via CMDB, config files, APIs, etc.)
* Maybe convert the nginx logic from Rexfile into a module (e.g. Rex::CodeMaven::Nginx)
* add a cert to nginx (e.g. via Let's Encrypt)
* Enable basic auth in nginx
* Write a script that will create a new Droplet with my own personal public key. This is going to be the management host.


## Getting started with Rex

* <a href="">Install Rex</a>
* Set up a remote host. e.g. Create a Droplet on [Digital Ocean](https://www.digitalocean.com/?refcode=0d4cc75b3a74)
* Make sure you can ssh to the host without providing a password.
* Run your first command using Rex: (after replacing USER by the remote username and REMOTE_HOST by the IP or dns name of the remote host.)

```
rex -u USER -H REMOTE_HOST -e 'say run(q{hostname})'
```

## Get remote hostname using Rexify

```
rex -u USER -H REMOTE_HOST -e 'say run(q{hostname})'
```

The output will look like this:

```
[2021-03-23 19:11:22] INFO - Running task eval-line on REMOTE_HOST
HOSTNAME
[2021-03-23 19:11:28] INFO - All tasks successful on all hosts
```

## List directory on remote host using Rexify

```
rex -u USER -H REMOTE_HOST -e 'say for run(q{ls -l})'
rex -u USER -H REMOTE_HOST -e 'say scalar run(q{ls -l})'
```

## Create a Rexfile

{% include file="examples/rex/minimal/Rexfile" %}

This is still useless, but we already have a Rexfile that declares its featureset.

## Rexfile with simple task showing remote hostname

{% include file="examples/rex/hostname/Rexfile" %}

<b>cd</b> into the directory of this file.

Then type in

```
rex -T
```

it will print out the list of available tasks in the Rexfile.

```
Tasks
 print_hostname  Just printing hostname
```

The output will look like this: (you need to replace USER and REMOTE_HOST and it will show something else instead of HOSTNAME

```
$ rex -u USER -H REMOTE_HOST print_hostname
[2021-03-25 13:21:48] INFO - Running task print_hostname on REMOTE_HOST
HOSTNAME
[2021-03-25 13:21:54] INFO - All tasks successful on all hosts
```

## Rexify update list of packages

<b>apt-get update using Rexify</b>

{% include file="examples/rex/update/Rexfile" %}

## Rexify install Nginx

{% include file="examples/rex/setup-nginx/Rexfile" %}

You might first need to update the list of packages.



