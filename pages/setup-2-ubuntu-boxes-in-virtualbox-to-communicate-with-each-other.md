---
title: "Setup 2 Ubuntu boxes in VirtualBox to communicate with each other"
timestamp: 2018-03-11T17:30:01
tags:
  - VirtualBox
  - Linux
  - ping
  - ssh
published: true
books:
  - linux
author: szabgab
archive: true
---


In order to learn about networking and interaction between machines we'll need more than one Linux box.

In order to learn how to use Ansible we also need at least 2 boxes. One that runs Ansible, the manager computer,
and one that is being managed by Ansible. (If we can set up more of these, even better as then we can see how to
configure different machine to do different tasks.) The ideal for some of our examples will be 4 machines.


We are going to set up multiple Virtual Boxes using Ubuntu Server. The default installation
uses 2.3 Gb disk, but it will quickly grow to 3-3.5 Gb. So make sure you have enough space for all the machines.
For 4 machines make sure you have at least 14 Gb space.

BTW the actual disk images are by default in the `~/VirtualBox\ VMs/` on my Mac. You can check the disk sizes there.

Install a Virtual box using Ubuntu as described in the beginning of the [Linux series](/linux). If you already
have one machine you can use that.

As a default name I used "Foo Bar" and the user "foo", so the text will assume that. If you use a different username, you'll
have to adjust some strings.

[Configure the host-only network](/virtualbox-host-only-network-ssh-to-remote-machine).
The IP of the host machine will be 192.168.56.1.
I used `ubuntu-ansible` as the hostname of the box I installed.
In the `/etc/network/interfaces` I set the IP address to be 192.168.56.2.

Once the box is ready, log in and [upgrade it](/upgrade-linux-packages-and-install-new-ones).

```
$ sudo apt-get update
$ sudo apt-get upgrade
```

Once we have one box ready, we can clone it, so we don't have to go over the installation and basic configuration process with each
one.

If you find all this work exhausting, you are right.
Just remember, currently we are doing the initial configuration manually.
Later on we'll be able to automate that part as well.
For now however it might be better for you to do all the steps manually so you better understand them and
you'll be able to experiment with them.

## Reduce memory allocation

If our physical computer only has 4 Gb memory then you won't be able to run 4 boxes of 1 Gb each.
If this setup is mostly to experiment with networking and/or Ansible, then we don't need that much memory
for the boxes anyway. So before I cloned the boxes I configured the one I have to have only 256 Mb memory.

For this I had to shut down the linux box. Select the machine in the VirtualBox gui. Click on Setup.
Select the "System" tab, and adjust the memory.

## Clone the VM

Shut down the Ubuntu box (`sudo shutdown -P now` will work well.)

On the VirtualBox management interface select your box, use the right-click `Clone` menu item. 
(If it is disabled, it means your machine is still running.)

Type in a name for the new box. Select <b>Full clone</b>.

The cloning itself will take a minute or more depending on the speed of your hard-disk and the size of the image.

## Configure machines: hostname, IP address

From the point of view of the VirtualBox now each machine has a name and each machine has its own disk.

From the inside however these two machines are identical. Same hostname, same IP address.

Boot the newly cloned machine and log in as user "foo".

Edit the `/etc/network/interfaces` file and change the IP address.

```
$ sudo nano /etc/network/interfaces
```

Edit  the `/etc/hostname` file and change the hostname.

Edit  the `/etc/hosts` file and adjust the hostname there as well.

Then reboot this machine `sudo reboot`, login again and verify that the
changes took place.

You could actually do this without rebooting the box, (eg. with `sudo hostname your-new-name`)
but it is cleaner that we do it with a reboot. That verifies that even after reboot the values will be set as we wanted them.

Here is my setup:
I make sure that the VirtualBox name (the one that we can see in the GUI of VirtualBox) and the hostname internally are the same for every machine. That makes it easier to identify them.


```
Hostname        IP
ubu-main    192.168.56.2 
ubu-box-1   192.168.56.11
ubu-box-2   192.168.56.12
ubu-box-3   192.168.56.13
```

## Verify Networking among the Virtual boxes

Once you have all the machines configured and checked you can see how the whole system works as a remote system.
From your host machine (your Windows or OSX machine) ssh to the main ubuntu machine using the command line ssh client on OSX:

```
ssh foo@192.168.56.2
```

or Putty on Windows.

Once you logged in to the main machine, check if you can ping the IP address of each one of the other boxes.
Stop it by pressing Ctrl-C:

```
$ ping 192.168.56.11
ING 192.168.56.11 (192.168.56.11) 56(84) bytes of data.
64 bytes from 192.168.56.11: icmp_seq=1 ttl=64 time=0.806 ms
64 bytes from 192.168.56.11: icmp_seq=2 ttl=64 time=0.448 ms
^C
```

## Enable passwordless ssh

From now on we are going to work on the main machine only and we'll want to be able to access the boxes using ssh
from the main machine without typing in a password.

First try to ssh:

```
ssh 192.168.56.11
```

It will first ask for a `yes` and then for a password. As these machines were all cloned from one single machine,
they all have user `foo` and the same password.

If that ssh worked, then log out (type `exit` or `Ctrl-d`).

Then [create an ssh-key and deploy it on each box.](/generate-and-deploy-ssh-private-public-keypair)

