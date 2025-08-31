---
title: "Docker course: Install Docker"
timestamp: 2022-10-25T10:04:01
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


Hello and welcome to the Docker course of Code-Maven. My name is Gabor Szabo.


{% youtube id="3CbPCOx7-B0" file="english-docker-course-install-docker.mkv" %}


The [slides](https://code-maven.com/slides/docker/) are in the usual place and we are
jumping ahead to the current slide: [Install Docker](https://code-maven.com/slides/docker/install-docker).

In order to use Docker you need to install it on your computer. On your local computer.

There are instructions on how to install Docker on all 3 of the major operating systems.
Here is the [link](https://docs.docker.com/get-docker/) to them.
Just click on it to get to the place where you can download and install Docker from.

Obviously this page will change as time goes on. This time you can see you can install

* Docker Desktop for Mac.
* Docker Desktop for Windows
* Docker for Linux.

The best is to follow the instructions there.

I'd like to point out a couple of things.

You could install Docker using <b>apt-get</b> or <b>yum</b> depending on the distribution of your Linux Operating System,
but probably it is better to use the installation method suggested in the Docker link because that way you'll get a better,
a newer version of Docker.

An one more thing for Linux. There is a link to the [post installation for Linux](https://docs.docker.com/engine/install/linux-postinstall/).

This is especially important if you start running Docker.

Normally you should be using your Linux machine as a regular user and not as root, but Docker needs special rights so it can access the kernel
in a special way. It is better not to run Docker as root so here some instructions on how to run Docker as non-root user.
So I am recommending that you follow these instructions. That's for Linux.

For Windows there are other things. Depending on the version of Windows you might be able to install the <a href="https://docs.docker.com/desktop/install/windows-install/"><b>Docker Desktop for Windows</b></a>
but there might be problems, especially if you are using older versions of Windows. In that case you might need to use the older version.

You have to check which version is working for you. In a minute or so we are going to see how you can actually check it out.

You can use the Command Prompt by running <b>cmd</b> and there you can type the <b>docker</b> command to see that Docker actually runs on your system.

We will have a separate recording especially for Windows, but for now let's hope that it already works for you.









