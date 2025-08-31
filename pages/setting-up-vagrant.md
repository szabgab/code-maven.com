---
title: "Getting started with Vagrant to set up a virtual environment"
timestamp: 2015-05-28T10:05:01
tags:
  - Vagrant
published: true
author: szabgab
archive: true
---


[Vagrant](https://www.vagrantup.com/) makes it very easy to install and manage virtual environments on your computer.
With just a few commands it can launch a Virtual Private Server on your desktop/laptop computer in which you can
freely install anything without interfering with other environments. Then you can as easily clean up and
remove that virtual environment.


## To Set up a Virtual Environment

Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
then go back to the [home page of Vagrant](https://www.vagrantup.com/) and follow the Getting Started instructions.

I have the following versions:

```
$ vagrant -v
Vagrant 1.7.2
```

```
$ VBoxManage -v
4.3.24r98716
```

Once I installed those two I run the following:

Create the directory where I am going to have the configuration files for this Vagrant instance.

```
mkdir ~/work/try
cd ~/work/try
```

Create a file called `Vagrant` in the current directory with some default parameters and indicate that you want to
have your environment based on the `hashicorp/precise32` which is a generic environment you can start with.
(If you'd like to have a more Perl-specific environment check out the article on
[Vagrant Perl Development Environment](/pro/vagrant-perl-development-environment).

```
vagrant init hashicorp/precise32
```

Launch the server. The first time we run this, it will download the necessary VirtualBox image file which can take some time.

```
vagrant up
```

ssh to the machine running on your desktop:

```
vagrant ssh
```

## Do your experiments

Now you are inside the VirtualBox image. You can freely install stuff, make changes everywhere except in the `/vagrant` directory.
With that directory you need to be careful becase that is mapped to the directory where you set Vagrant up. (In our case that is the `~/work/try`
directory.)

This virtual environment is based on Ubuntu.

As Ubuntu gets security and other fixes almost on daily basis, the first thing you might want to do is to update all the packages:

```
vagrant@precise32:~$ sudo aptitude update
vagrant@precise32:~$ sudo aptitude -y safe-upgrade
```

For me it has installed 181 packages.

Once this is done, you'd need to restart the virtual environment for all the changes to take effect.
(I have not checked, but I am quite sure there is at least one update that really requires a reboot.)

Exit the ssh session:

```
vagrant@precise32:~$ exit
```

Stop your virtual instance:

```
vagrant halt
```

Start it again:

```
vagrant up
```

ssh to it again:

```
vagrant ssh
```

Then install whatever you'd need

```
vagrant@precise32:~$ sudo aptitude install ....
```

A few things that I usually need:

```
vagrant@precise32:~$ sudo aptitude -y install curl vim
```


## Destroy

After you are done using the virtual environment you can leave the box by typing

```
vagrant@precise32:~$ exit
```

Then you can completely remove all traces of your changes using the following command:

```
vagrant destroy
```

This will still keep the original `hashicorp/precise32` image, taking up some space
on your hard disk, but it means next time you runt `vagrant up` it will be much faster
as it won't need to donwload any files.

