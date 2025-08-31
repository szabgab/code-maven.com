---
title: "Convert any script to a Linux service (daemon)"
timestamp: 2022-08-21T09:30:01
tags:
  - systemctl
  - daemon
  - service
  - syslog
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


A <b>service</b> or in Unix/Linux terms a <b>daemon</b> is a program that continuously runs in the background.
Sometimes it listens to some port or some events and based on the input does something.
Sometimes it uses the internal clock of the computer to execute some functions periodically.


{% youtube id="nyPrRKHMYzY" file="convert-to-linux-daemon.mp4" %}

There are many well known services that either run on your computer by default or you can install them.
The former might be the service waiting for you to type in your username and password on the terminal to log in,
or waiting for an ssh connection, or running your cron jobs. The latter might be a web-server, a database server.
(Things that are called servers are usually installed as services so they would run in the background.)

Services are usually configured to start when the computer boots up to be able to provide service even without
the login of any user.

## How can we create a service / daemon?

The following file is just a very simple script that will print the timestamp in a file every 1 second.
There is noting special about it.

{% include file="examples/daemon/timestamp.py" %}

You can run the script on the command line:

```
python examples/daemon/timestamp.py
```

and then in a <b>separate terminal</b> you can observe the file growing by running the following command:

```
tail -f /tmp/timestamp.log
```

In order to stop the script you need to switch back to the first terminal and press <b>Crtl-C</b>.

Then you can try to run the script with some parameter. e.g.:

```
python examples/daemon/timestamp.py hello
```

And switch to the 2nd terminal to observe the output.


## The service / daemon configuration file

In order to turn this into a service we need to create a service configuration file:

{% include file="examples/daemon/timestamp.service" %}

The most important field here is:

<b>ExecStart</b>

Create a symbolic link from the system-wide location of all the services in <b>/usr/lib/systemd/system/</b>
to the place where our service configuration file is. (Alternatively you could also copy the <b>timestamp.service</b> file.

```
sudo ln -s /home/gabor/work/code-maven.com/examples/daemon/timestamp.service  /usr/lib/systemd/system/timestamp.service
```

Then we need to tell the <b>daemon-service</b> no reload all the configuration files. We need to do this every time we
add a new service or change the configuration file of a service.

```
sudo systemctl daemon-reload
```


Then we can <b>start the service</b>

```
sudo systemctl start timestamp.service
```

At this time we should be able to use the <b>tail</b> command to observe how the service works and the file grows
one line every second.

```
tail -f /tmp/timestamp.log
```


## Troubleshooting pitfalls, potential issues and fixes

If you the timestamp.log file does not grow you it means we had some issues.

You can observe the status of the service by running the following command:

```
sudo systemctl status timestamp.service
```

You can also look at the log in the <b>syslog</b> file:

```
less /var/log/syslog
```



While writing this article I had two issues:

## Issue one: typo in command

At first I had a typo in the command on the ExecStart line. That was easy to fix.

## Issue two: rights on the log file

Even after the typo was fixed I still did not see the log file growing.



```
sudo systemctl status timestamp.service
```

got me this output:

```
× timestamp.service - Demo Service
     Loaded: loaded (/lib/systemd/system/timestamp.service; disabled; vendor preset: enabled)
     Active: failed (Result: exit-code) since Sun 2022-08-21 09:35:46 IDT; 7s ago
    Process: 2046747 ExecStart=/usr/bin/python3 /home/gabor/work/code-maven.com/examples/daemon/timestamp.py mydaemon (code=exited, status=1/FAILURE)
   Main PID: 2046747 (code=exited, status=1/FAILURE)
        CPU: 119ms

Aug 21 09:35:46 code-maven systemd[1]: timestamp.service: Scheduled restart job, restart counter is at 5.
Aug 21 09:35:46 code-maven systemd[1]: Stopped Demo Service.
Aug 21 09:35:46 code-maven systemd[1]: timestamp.service: Start request repeated too quickly.
Aug 21 09:35:46 code-maven systemd[1]: timestamp.service: Failed with result 'exit-code'.
Aug 21 09:35:46 code-maven systemd[1]: Failed to start Demo Service.
```

Then I looked at the syslog:

```
less /var/log/syslog
```

and saw this:

```
Aug 21 09:37:44 code-maven python3[2047136]:   File "/home/gabor/work/code-maven.com/examples/daemon/timestamp.py", line 11, in <module>
Aug 21 09:37:44 code-maven python3[2047136]:     with open("/tmp/timestamp.log", "a") as fh:
Aug 21 09:37:44 code-maven python3[2047136]: PermissionError: [Errno 13] Permission denied: '/tmp/timestamp.log'
```

Apparently the daemon that is currently configured as user root does not have permissions to open the log file for writing.

```
$ ls -l /tmp/timestamp.log
-rw-rw-r-- 1 gabor gabor 504 Aug 21 09:35 /tmp/timestamp.log
```

At this point I could have changed the configuration file of the service to run as user <b>gabor</b>,
I could have changed the right on the file so everyone can write to it.

I decided to get rid of the file and let the daemon create it by itself:

```
$ rm -f /tmp/timestamp.log
```

Then I started the daemon again. This time it started to work.


```
$ sudo systemctl status timestamp.service

● timestamp.service - Demo Service
     Loaded: loaded (/lib/systemd/system/timestamp.service; disabled; vendor preset: enabled)
     Active: active (running) since Sun 2022-08-21 09:54:13 IDT; 3s ago
   Main PID: 2049558 (python3)
      Tasks: 1 (limit: 18981)
     Memory: 3.5M
        CPU: 26ms
     CGroup: /system.slice/timestamp.service
             └─2049558 /usr/bin/python3 /home/gabor/work/code-maven.com/examples/daemon/timestamp.py "my daemon"

Aug 21 09:54:13 code-maven systemd[1]: Started Demo Service.

```


I can observe the file as well. Now it is owned by user root:

```
$ ls -l /tmp/timestamp.log
-rw-r--r-- 1 root root 4508 Aug 21 09:54 /tmp/timestamp.log
```


## Stop the service

```
sudo systemctl stop timestamp.service
```

## Restart the service

```
sudo systemctl restart timestamp.service
```



## Conclusion

It is very easy to convert a script to a daemon, but one needs to be careful with the rights on files and also the environment
that is different for a daemon and for a script that runs on the command line.

We only scratched the surface of the daemonization. There are tons of other options you can deal with, but this should already
get you started.

