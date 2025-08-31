---
title: "Use Docker both as regular user and as root (with or without sudo)"
timestamp: 2023-04-27T07:30:01
tags:
  - Docker
  - sudo
published: true
books:
  - docker
author: szabgab
archive: true
show_related: true
---


The problem I encountered with the solution to [create a file on a mounted volume in Docker as the external user (and not as root)](https://code-maven.com/creating-file-in-docker-as-the-external-user) was that using a regular user internally made it impossible to execute commands as root. In particular it made it impossible to install packages using the package-management system of the operating system.


This is not a problem during regular software development because you rarely need to install extra system-packages. Most (all?) programming languages have a tool to install their own packages as regular user.
However, there are cases, especially when you first try to create a Docker image to run a particular piece of software, that you will need to install several system-level packages and also run the code of the project that might create files in the current working directory which is mapped to the external disk.

I found two solution for this. Both involves switching between regular user and root user but they work in different ways.

The first solution does not need any extra installation, but you probably need more self-discipline and in a way I feel it is more error-prone.

The second needs us to install <b>sudo</b>.

## Without sudo

In this version we return to launching Docker and being user <b>root</b> inside.

```
$ docker run -it -w /opt -v$(pwd):/opt --name ubu ubuntu:23.04 bash
```

Now we are user <b>root</b>. At this time we can install extra packages. e.g. installing <b>less</b>:

```
# apt-get update
# apt-get install -y less
```

The we can switch to the regular <b>ubuntu</b> user and work as regular user inside Docker (e.g. create a file in the folder that was mapped to the external disk):

```
# su - ubuntu
$ cd /opt
$ touch hello
```

If we would like to install another system-wide package, we need to use <b>exit</b> to leave the <b>ubuntu</b> user, then we can install more packages and can get back
to our regular user again with <b>su - ubuntu</b>. (The <b>-</b> tells Linux to set up the full environment of that user.)

In order to leave the Docker container we need to execute <b>exit</b> twice. First to <b>exit</b> the regular user to become root and then to <b>exit</b> the container.


## With sudo

For this solution we need a little-bit of setup. We have the following <b>Dockerfile</b>:

{% include file="examples/docker-sudu/Dockerfile" %}

* We install <b>sudo</b>.
* Add the user <b>ubuntu</b> to the group that can use sudo.
* We add <b>ubuntu</b> to the sudoers file and allow it to execute commands without providing a password.

We build the image:

```
docker build -t myubuntu .
```

Then run it as the user <b>ubuntu</b>

```
docker run -it -w /opt -v$(pwd):/opt --name ubu --user ubuntu myubuntu bash
```

Now we use it as the regular user <b>ubuntu</b>.

```
$ touch file_in_mounted_folder
```

If we would like to install as system-wide package we can use sudo:

```
$ sudo apt-get update
$ sudo apt-get install -y less
```

When we would like to exit we need to type <b>exit</b> only once.


