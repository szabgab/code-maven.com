---
title: "Run code locally with Rexify"
timestamp: 2021-04-11T10:00:01
tags:
  - no_ssh
  - LOCAL
  - Rex
  - Rexify
description: "Run code locally while working with Rex"
published: true
books:
  - rex
author: szabgab
archive: true
show_related: true
---


Usually you'll want your Rex commands to be executed on the remote server and thus the default of Rexify is to execute the rex command on the current remote server.
However sometimes you'd want to have some Rex commands executed locally. There are two main ways to to that, either marking the task as `no_ssh` or
marking a secion of the task as `LOCAL`.

Also remember that the perl code around the Rex commands are always executed locally on the management server.

This example demonstrates these cases:


{% include file="examples/rex/local/Rexfile" %}

In our example the hostname of the managemachine was <b>code-maven</b> and the name of the remote server was <b>rex-host</b>.

```
$ rex -H 104.236.89.4 -u root remote
[2021-04-11 09:50:50] INFO - Running task remote on 104.236.89.4
[2021-04-11 09:50:54] INFO - Sys::Hostname::hostname() is always the local machine: code-maven
[2021-04-11 09:50:55] INFO - run('hostname'): rex-host
[2021-04-11 09:50:55] INFO - All tasks successful on all hosts
```


```
$ rex -H 104.236.89.4 -u root local
[2021-04-11 09:51:11] INFO - Running task local on 104.236.89.4
[2021-04-11 09:51:11] INFO - Sys::Hostname::hostname() is always the local machine: code-maven
[2021-04-11 09:51:11] INFO - run('hostname'): code-maven
[2021-04-11 09:51:11] INFO - All tasks successful on all hosts
```

```
$ rex -H 104.236.89.4 -u root partial
[2021-04-11 09:51:20] INFO - Running task partial on 104.236.89.4
[2021-04-11 09:51:24] INFO - Sys::Hostname::hostname() is always the local machine: code-maven
[2021-04-11 09:51:24] INFO - run('hostname'): rex-host
[2021-04-11 09:51:24] INFO - Sys::Hostname::hostname() is always the local machine: code-maven
[2021-04-11 09:51:24] INFO - run('hostname'): code-maven
[2021-04-11 09:51:24] INFO - All tasks successful on all hosts
```


See also: [no_ssh](https://metacpan.org/pod/Rex::Commands#no_ssh)

