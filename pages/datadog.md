---
title: "Datadog"
timestamp: 2020-09-17T19:30:01
tags:
  - DataDog
  - monitoring
description: "DataDog is the leading provider of application and infrastructure monitoring service. This is just my notebook for using DataDog"
published: true
author: szabgab
archive: true
show_related: true
---


This posts is here only to collect some of the notes I have about Datadog. With time it might become a more comprehensive post.


## Setup

Create an account and install the agent on one of your servers. It will immediately start sending generic system-related metrics.
eg. cPU load, memory usage, disk IO, Network etc. It will also start sending metrics about itself.



## Datadog command line tools

It is written in Python so you install it with the following command:

```
pip install datadog
```

Get the API  key and Application key from your [account settings](https://app.datadoghq.com/account/settings).
You can then save them in ~/.dogrc but when you run `dog` on the command line it will ask for the values and save them
in the config file for you.

```
[Connection]
apikey = AAAAAAAAAAAAAAAAAAA
appkey = BBBBBBBBBBBBBBBBBBBB
```

## Submit an event from the command line

```
dog event post "Command line title" "command line text"
```

Then see it on your [event stream](https://app.datadoghq.com/event/stream).

<h3>Post some metric</h3>

```
dog metric post foobar.test 1
dog metric post foobar.test 2
```


