---
title: "Installing Ansible"
timestamp: 2018-03-14T19:40:01
tags:
  - Ansible
  - pip
published: true
author: szabgab
archive: true
---


Before you can start using Ansible you need to install it on the management machine.

Ansible runs on Linux/Unix machines including Mac OSX. (There is no plan to port it to run on MS Windows.) This is the manegement machine.

It can control (manage) both Linux/Unix machines and boxes running MS Windows.


Your notebook or some in-house machine in the company can work. If you only have Windows machines you can install Linux as a virtual
environment. e.g. [Ubuntu Linux in VirtualBox](/installing-ubuntu-linux-in-virtualbox).

One thing you need to remember about security is that the user who can run ansible will have
virtually unlimited control of all your servers. So make sure the account that is set up to run ansible has adequate
authentication set up.

I am setting it up on my Macbook air in my own account. I am going to use my own public key to allow me access to the privileged
user on the servers. I'd better not share my private key with anyone then.

There are a number of ways to [install Ansible](http://docs.ansible.com/ansible/latest/intro_installation.html).

Ansible is written in Python and as I already have Python 3 installed on my machine I went with `virtualenv` and `pip` here.


<h3>Setting up Virtualenv on Ubuntu 17.04</h3>

If you have a bare-bones Ubuntu 17.04 then this is how you set up a virtualenv for python3:

```
$ sudo apt-get install virtualenv python3-virtualenv python3-pip
$ virtualenv venv --python=python3
```

<h3>Setting up Ansible on Ubuntu 17.04</h3>

Once you have the virtualenv set up you need to activate it and then you can install Ansible using `pip`.

```
$ source venv/bin/activate
$ pip install ansible
```

After a while I had Ansible installed.

```
$ ansible --version
```

Shows the version number of Ansible. (I have 2.4.1.0) with some additional information.

```
$ ansible -h
```

provides help. It lists many of the parameters we can use with the `ansible` command.

More to come soon.

<img src="/img/ansible-logo.jpg" alt="Ansible logo">

