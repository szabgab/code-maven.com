---
title: "Docker uses a lot more disk-space than docker system df reports"
timestamp: 2024-01-04T08:30:01
tags:
  - docker
description: "Docker system df can provide detailed reports on disk usage but it does not include the disk space used by the log files."
published: true
books:
  - docker
author: szabgab
archive: true
show_related: true
---


<b>docker system df</b> shows a nice overview of the disk-space usage of the Docker installation.

Like this:

```
$ docker system df
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          7         2         5.129GB   4.806GB (93%)
Containers      3         3         12.46MB   0B (0%)
Local Volumes   4         3         7.627GB   230MB (3%)
Build Cache     165       0         2.378GB   2.378GB
```



Using the <b>-v</b> flag like this : <b>docker system df -v</b>  shows the same information in way more details that can help you understand what part of Docker uses all that data.

Except in my case, the folder where Docker stored its data used about 20 times more space than reported by Docker.
Naturally I only noticed it when my server ran out of disk-space putting me in panic-mode.

It took me a while till I realized there are some huge log-files in the <b>containers</b> folder.

I am sure you know that you can look at the output that was printed to the console of your container by running the command:

```
docker container logs NAME_OF_A_CONTAINER
```

As it turns out this output is saved in a file in the folder of the individual container and <b>by default it is kept forever</b>.

<b>docker system df</b> can provide detailed reports on disk usage, but it does <b>not</b> include the disk space used by the log files.

One of the services I used was very, I mean really talkative and printed tons of stuff on the console. Docker shoved all of that into an ever growing file.

## Solution

The immediate solution was to stop docker and remove the huge file.

The longer-term solution was to configure Docker to keep the log files limited in size.

It can be done in the daemon configuration file which, at least in my installation is located in

```
/etc/docker/daemon.json
```

I already had this in the file:

```
{
    "data-root": "/home/data/docker",
}
```

That's because a while ago I moved all the data to a disk separate from the disk of the operating system.

Now I updated it:

```
{
    "data-root": "/home/data/docker",

    "log-driver": "json-file",
    "log-opts": {
        "max-size": "10m",
        "max-file": "3"
    }
}
```

Then I restarted the Docker daemon with

```
sudo systemctl restart docker
```

and I also had to <b>stop and remove the existing containers and start new ones</b>!

Without that the changed did not take effect.


To tell the truth I also rebooted the host machine. It is probably not necessary, but I like to do that after such changes to verify that
the computer can be booted and all the services start as expected. I rather have a few seconds downtime when I still remember the
changes I made than later when something breaks because of some changes a few weeks or month earlier.

For more details see how to [configure logging drivers for Docker](https://docs.docker.com/config/containers/logging/configure/).



