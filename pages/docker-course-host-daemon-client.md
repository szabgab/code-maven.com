---
title: "Docker course: host - daemon - client"
timestamp: 2022-11-08T06:02:01
tags:
  - Docker
types:
  - screencast
published: true
books:
  - docker
author: szabgab
archive: true
show_related: false
---


In this episode we are going to learn about [Docker host, daemon, and client](https://code-maven.com/slides/docker/docker-host-daemon-client).

These are 3 entities involved in running Docker.


{% youtube id="6khOMKZ2Ny0" file="/english-docker-course-host-daemon-client.mkv" %}

## Docker host

Docker host is where at the end the Docker container will run. If your computer runs Linux then the Docker host is native.
It runs directly on your Linux machine. However if your container is a Linux-based container then on Windows and Mac OSX
it needs a Linux-based virtual machine to run on. So in this case we will have a virtual machine running on top of the operating
system that runs on our computer.

This means the performance is not going to be as good as if you were running it natively on Linux, but then on top of this
host, on the top of this virtual machine that runs on Windows or on OSX, you can have several Docker containers running.


## Docker Daemon

There is a <b>docker daemon</b> which is running on the host itself so it does not matter if your operating system is Linux or Windows or OSX
it is running on top of the host.

## Docker Client

Finally there is the Docker client, the one that you are actually interacting with, so when you type in <b>docker</b>, that's the Docker client
and that too runs on your Operating System that can be either Linux, OSX, or Windows.

So docker Daemon runs on the host, but the Docker client can run on another machine.
So one machine can have the client and then it can connect to the daemon running on some other host.

In this course we are going to run client and daemon on the same computer. So it's easier.

How do you start the daemon? You need to start the daemon in order to talk to it. The client you just type in <b>docker</b> and press ENTER. That's the client.

So we need to start the daemon which is just the Docker server. (For our purposes a daemon is just another word for a server.)

How do you do that?

It is depending on your installation.

In some cases the installation will configure the Docker daemon to start automatically when the computer boots. Depending on your use-case this might be the
preferable solution.

Sometimes you might prefer that it won't start together with the Operating System, so it won't use resources when you don't need it.
In that case you need to manually start the daemon.

On OSX you need to type in

```
open -a Docker
```

to launch the Docker daemon.

On Linux you'd probably write

```
sudo service docker start
```

On Windows you'll have an icon of the <b>Docker Desktop</b>. Just run that. It takes some time, maybe a minute to start it, but then the daemon is running.

Then you can use the Docker client (the <b>docker</b> command) in order to connect to the daemon and give it instructions.
Run those command that we saw in the help.

I think we have one more episode (video) before we start actually doing things with Docker because I'd like to talk a bit about the Docker Registry
before we start using Docker.
