---
title: "Upgrade Linux packages and install new ones"
timestamp: 2018-03-11T11:00:01
tags:
  - apt-get
  - sudo
published: true
author: szabgab
archive: true
---


Once you [installed Ubuntu in VirtualBox](/installing-ubuntu-linux-in-virtualbox) let's now see how
can we install new packages and upgrade the existing ones.



## Login

I assume you have [just installed](/installing-ubuntu-linux-in-virtualbox) your Ubuntu system,
saw the login screen

![](/img/vb1/linux_install_3.png)

typed in your usernane and password and now you see the Linux terminal with a prompt:

![](/img/vb1/linux_login_1.png)

(You might have a lot more text on the screen above that line, but the prompt is usually recognizable as it ends
with a `$` character for regular users and the `#` character for the superuser (administrator) called `root`.)

At this point you will be able to type in commands.

e.g. `ls` will list the content of the current directory. In our case it did not show anything as there are
no visible files in the current directory.

The `pwd` command will print the path to the current directory which is `/home/foo` in our example.

The `whoami` command will print the username of the user who is currently logged in to this terminal.

![](/img/vb1/linux_login_2.png)

Let's now discuss another topic and then get back using the command line:

## Package repositories

Unlike on MS Windows, in Linux additional software is usually installed from a few central places.
Much like what you are used to on your mobile phone.

On Android you have the Google play store, on Apple products you have the Appstore. They were both modeled after the package-management systems that are used for Linux distributions.

When we [installed Ubuntu](/installing-ubuntu-linux-in-virtualbox) we installed a few hundred (maybe thousand) packages. The standard Ubuntu package store contains 10s of thousands of additional packages. Some are libraries, some are servers (e.g. web server, database server), some are desktop applications (e.g. browsers, word processors, spreadsheet tools, games).

Each Linux distribution has its own package stores, but there are two major packaging systems. 
The distributions that are derivatives of Debian (e.g. Ubuntu, Mint) use files with `deb` extension and the `apt` family of commands to manage them.
Other distributions (RedHat, Fedora, CentOS) use files with `rpm` extension and the command `rpm` or `yum`.

There are probably other commands as well, this is far from a comprehensive overview.

## Users

On a Linux system each human user usually has his/her own user account. Applications that provide services usually also have their own user (e.g. MySQL server has a user called mysql). The user system is used to allocate certain rights to individual users or services,
or if you like, to limit the rights of users and services. This is great as it allows us to provide security. e.g. a regular user should not be able to install new software or change the configuration of a web server. Even the web server should not be able to changes it own configuration.

There is also a user called `root` that can do anything in the system. It can install software, configure web server, add and remove users and set the rights of all the other users.


Even if you are a system administrator who could use the `root` user, normally you'd use your own Linux user to limit the impact of mistakes. You would only "become root" when it is necessary. In older systems this would mean that you login as user `root` usually with a command called `su`.

In modern systems the usual way is to use the `sudo` command to execute individual commands as user `root`. This further reduces the chance of us making a fatal mistake while acting as user `root`.

Normal users cannot use the `sudo` command, but when you installed Ubuntu, the user you created automatically got the rights to use the `sudo` command to do anything. Including to create new uses and to give them the right to use `sudo`.

## Updating the packages

Just as for your mobile phone, the Linux distributions also keep updating the packages in the package repository.
There is a big difference though as the Linux distributions usually only update package for security issues and bug fixes
so updating the system with new package usually don't introduce any new problems.

When we installed Ubuntu we used and ISO image that was created a few weeks or months ago. Since then many packages might have been updated in the repository. Let's update them on our box as well.

In Ubuntu we need two steps for this. The first step updates the list of packages available, the second step actually upgrades the packages. Let's update the list:

```
apt-get update
```

The response is this:

![](/img/vb1/linux_login_3.png)

It tried to update the list but failed.

The reason is that tried to create a file in a directory called `/var/lib/apt/list` but I ran `apt-get` as my regular user (foo in this case) it did not have the permissions to write there.

We need to use `sudo` to execute the command:

```
sudo apt-get update
```

First it ask for the password of your user "foo" and then it updates the list of available packages.

![](/img/vb1/linux_login_4.png)


Then we can upgrade the packages using

```
sudo apt-get upgrade
```

Normally this `sudo` command also asks for your password, but in order to make the system more usable `sudo` will only ask for them if a certain amount of time has passed since you used it last time.

So if you need to execute several command in a short time-span it won't annoy you by asking the password for every command.

The first output might look like this though it might have a much longer list. In any case, before downloading and installing the
packages it will ask you if you'd want to proceed.

![](/img/vb1/linux_login_5.png)

click on `Y` and `ENTER` and the process will continue, download and install all the modules and get to the prompt again:

![](/img/vb1/linux_login_6.png)

## Installing new software

In order to install a new package, eg. the package called `ssh` you need to type:

```
sudo apt-get install ssh
```

This will ask you if you really want to install it and if you say yes then it will install the package and all its dependencies.




