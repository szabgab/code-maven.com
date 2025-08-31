---
title: "Ansible on Ubuntu in VirtualBox environment - using Python 3"
timestamp: 2018-03-14T11:30:01
tags:
  - Ansible
  - Ubuntu
  - Python
published: true
books:
  - ansible
author: szabgab
archive: true
---


In this article we'll set up Ansible on our new Ubuntu-based managers machines and will use Ansible to access (ping) a remote machine that is also bare-bones Ubuntu 17.04.


Set up two or more VirtualBoxes using Ubuntu. See the [Linux series](/linux) for step-by-step instructions.
Including setting up ssh key on `ubu-main` and copying it over to `ubu-box-1` so we can freely ssh
from `ubu-main` to `ubu-box-1`.

`ubu-main` at 192.168.56.2 will be the box we use for management.

`ubu-box-1` at 192.168.56.11 will be one of the hosts we would like to manage.

Log in to `ubu-main` and [install Ansible](/ansible).



## Enable Ansible

From now on every time you would like to run ansible you'll log in to `ubu-main` and you'll have to load the Python virtualenv. It can be done by a simple command:


```
$ source venv/bin/activate
```

You don't need to run any of the other command we ran earlier, as those installations are all in this virtual environment.

In order to improve your work-environment you could also add the above line to the end of the `.bashrc` file in your home directory.

## Ping the host using ICMP

Given that we can already ssh into `ubu-box-1` this a bit unnecessary, but for the methodology, let's use the command line `ping` program to see if the "remote" host is accessible on the IP level: (Stop with Ctrl-C)

```
$ ping 192.168.56.11
PING 192.168.56.11 (192.168.56.11) 56(84) bytes of data.
64 bytes from 192.168.56.11: icmp_seq=1 ttl=64 time=0.370 ms
64 bytes from 192.168.56.11: icmp_seq=2 ttl=64 time=0.991 ms
64 bytes from 192.168.56.11: icmp_seq=3 ttl=64 time=0.976 ms
^C
--- 192.168.56.11 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2026ms
rtt min/avg/max/mdev = 0.370/0.779/0.991/0.289 ms
```

Just to show you how does it look like when the remote machine is not reachable with the command line `ping` I tried to ping another IP that is not in use. Again Ctr-C stops it.

```
$ ping 192.168.56.12

PING 192.168.56.12 (192.168.56.12) 56(84) bytes of data.
From 192.168.56.2 icmp_seq=1 Destination Host Unreachable
From 192.168.56.2 icmp_seq=2 Destination Host Unreachable
From 192.168.56.2 icmp_seq=3 Destination Host Unreachable
^C
--- 192.168.56.12 ping statistics ---
4 packets transmitted, 0 received, +3 errors, 100% packet loss, time 3057ms
pipe 4
```

## Ping the hosts using Ansible

Once we have Ansible installed, and we checked that it can be executed running

```
$ ansible --version

ansible 2.4.3.0
  config file = None
  configured module search path = ['/home/foo/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /home/foo/venv/lib/python3.6/site-packages/ansible
  executable location = /home/foo/venv/bin/ansible
  python version = 3.6.3 (default, Oct  3 2017, 21:45:48) [GCC 7.2.0]
```

the first thing to do is to check if we can reach the host(s) by Ansible.

We prepare a configuration file that will list our "inventory", the list of all the hosts we are managing.

`inventory.cfg` looks like this:

```
[all]
192.168.56.11
```

Now we can ping "all" the machines in our inventory by running:

```
$ ansible -i inventory.cfg all -m ping
```

```
192.168.56.11 | FAILED! => {
    "changed": false,
    "module_stderr": "Shared connection to 192.168.56.11 closed.\r\n",
    "module_stdout": "/bin/sh: 1: /usr/bin/python: not found\r\n",
    "msg": "MODULE FAILURE",
    "rc": 0
}
```

The `ping` module of Ansible is different from the `ping` command. It attempts to connect to the remote machines using `ssh` and then it tries to check if it will be able to execute code on the remote machines.

Our attempt failed because Ansible uses Python 2 to be installed on the remote machines in order to work and Ubuntu 17.04 comes with Python 3 only.

## Tell Ansible to use Python 3

Starting from version 2.2.0 of Ansible you can ask it to use Python 3 on the remote machine.


You can do it on the command line, but then you'll have to do it every time you run ansible:

```
$ ansible -i inventory.cfg all -m ping -e 'ansible_python_interpreter=/usr/bin/python3'
```


You can do it per machine in the inventory file:

```
[all]
192.168.56.11 ansible_python_interpreter=/usr/bin/python3
```

or you can do it for a group of machines in the inventory file:

```
[all]
192.168.56.11

[all:vars]
ansible_python_interpreter=/usr/bin/python3
```


## Install Python 2 on the hosts

Alternatively you could install Python 2 on each host and we could do it either manually or using Ansible. Here you can see how to
do it manually, if that's what you'd like to do.

Install Python 2 on the remote host manually: ssh to remote host and then run `sudo apt-get install -y python`.
This time I've included the full prompt to make it easier to see on which machine do I executed each command:

```
foo@ubu-main:~$ ssh foo@192.168.56.11
foo@ubu-box-1:~$ sudo apt-get install -y python
...
foo@ubu-box-1:~$ exit
```

If we try to ping now it should be successful:

```
$ ansible -i inventory.cfg all -m ping

192.168.56.11 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

## Remove Python 2

If you'd like to experiment with this, you can remove Python 2 manually with the following commands:

```
$ sudo apt-get remove --purge  python
$ sudo apt autoremove
```

You can check the availability of Python 2 by running:

```
$ python --version
-bash: /usr/bin/python: No such file or directory
```

as opposed to

```
$ python --version
Python 2.7.14
```

when Python 2 is installed.

Then you can see if your process installing Python 2 works.

## Ping with Ansible successful

In any case, you need to be able to successfully ping the remote host(s) in order to start using Ansible.

```
$ ansible -i inventory.cfg all -m ping

192.168.56.11 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```


