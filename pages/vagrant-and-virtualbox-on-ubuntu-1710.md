---
title: "Vagrant and VirtualBox on Ubuntu 17.10 and CentOS 7"
timestamp: 2018-02-20T15:30:01
tags:
  - Vagrant
  - VirtualBox
  - Ubuntu
  - CentOS
  - Linux
  - apt-get
  - yum
published: true
author: szabgab
archive: true
---


I have computer at home with 16Gb memory on which I've installed Ubuntu 17.10. It also has plenty of disk space, so it is going to be much better for experimenting with multi-server setups than my MacBook Air that only has 4Gb memory and 128 Gb SSD storage which is usually full.

While I could certainly sit at that Linux machine as a desktop, I opted to use it mostly to use it as a server and ssh into it.

Now in order to experiment with multiple server setups easily I needed Vagrant and VirtualBox and I wanted to install another Ubuntu as a guest operating system.


## Which version of Vagrant and VirtualBox?

I usually prefer to use the packages provided by the OS vendor, that could be installed using the standard package management system.
Unfortunately the version of Vagrant and VirtualBox that are packaged by Ubuntu are old and due to some changes in the web service provided by Hashicorp (the organization behind Vagrant) they don't work any more.

Instead of that I went with the latest and greatest:

## Install VirtualBox

Download the latest version of deb file from [VirtualBox Linux downloads](https://www.virtualbox.org/wiki/Linux_Downloads) and then run

```
sudo apt install ./virtualbox-5.2_5.2.6-120293~Ubuntu~zesty_amd64.deb
```

Certainly by the time you run this the version and so the name of the file will change.

## Install Vagrant

Download the .deb file for Debian from [Vagrant downloads](https://www.vagrantup.com/downloads.html) and then run:

```
sudo apt install ./vagrant_2.0.2_x86_64.deb
```


## Verify the installed versions

```
$ virtualbox -h
Oracle VM VirtualBox Manager 5.2.6
...
```

```
$ vagrant -v
Vagrant 2.0.2
```


## Create first Ubuntu-based VirtualBox using Vagrant

This is actually and older version of Ubuntu. Xenial Xerus is version 16.04 which is an LTS version.

```
$ mkdir ubuntu
$ cd ubuntu
$ vagrant init ubuntu/xenial64
$ vagrant up
$ vagrant ssh
```

That's it. I am inside the Virtualbox.

In order to have everything up to date I also ran:

```
$ sudo apt-get update
$ sudo apt-get upgrade
```


I can exit it using `exit` and then I can shut down the VirtualBox by running

```
$ vagrant halt
```


Note: The `intit` command created a file called `Vagrantfile` that contains
the configuration of the Vagrant image.

## Install Centos/7 based VirtualBox

Just to further my experiments I've also created a separate VirtualBox using CentOS 7.

For this I created a second directory as we'll need a separate `Vagrantfile`.

```
$ mkdir centos
$ cd centos
$ vagrant init centos/7
$ vagrant up
$ vagrant ssh
```

We can update it to the latest pacakges using:

```
$ yum update
```


