---
title: "Install and configure Nginx using Ansible"
timestamp: 2018-03-21T10:00:01
tags:
  - Ansible
published: true
books:
  - ansible
author: szabgab
archive: true
---


Probably one of the easiest and most straight forward things we can do using Ansible is to install and configure a web server.
Specifically Nginx.


Let's log in to our management machine and use `curl` on the command line to check if the web server on
our server is accessible:

```
curl http://192.168.56.11
```

The response is

```
curl: (7) Failed to connect to 192.168.56.11 port 80: Connection refused
```

because there is no web server on that box.

## Install Nginx on Ubuntu

We need to have inventory file that lists all the boxes we would like to manage.

```
[web]
192.168.56.11

[web:vars]
ansible_python_interpreter=/usr/bin/python3
```

Here we have a group called "web" (you can have any arbitrary name there) and the single remote machine is listed in that group.
The `ansible_python_interpreter=/usr/bin/python3` is there so Ansible will use Python 3 on the remote machine.

We create an Ansible Playbook which is just a YAML file:

{% include file="examples/ansible/nginx_install.yml" %}

In this playbook we have one task that has two steps. The "- name: ...." are only there for the humans, to make sense of the commands.
The first step `apt: name=nginx state=latest` tells the `apt` module that we want the latest version of the `nginx` package to be installed.
The next step tells Linux to make sure the `service` called `nginx` is `started`. (The `name: nginx` is part of the command.)
Interestingly on the current version of Ubuntu you don't need the latter as Ubuntu takes care of it, but it is better to explicitly say what is that state you require. Especially if you will ever want to uninstall and then re-install nginx.

I assume you've already [set up passwordless sudo](/enable-ansible-passwordless-sudo) so we don't need to supply the `-K` or `--ask-become-pass` flags.

```
$ ansible-playbook -i inventory.cfg nginx_install.yml -b
```

The `-b` tells ansible to become `root` on the remote server using `sudo`. The output looks like this:

```
PLAY [all] *******************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************
ok: [192.168.56.11]

TASK [ensure nginx is at the latest version] *********************************************************************
changed: [192.168.56.11]

PLAY RECAP *******************************************************************************************************
192.168.56.11              : ok=2    changed=1    unreachable=0    failed=0
```

Then we can try `curl` again. This time we get some HTML output that I have trimmed for brevity.
Apparently the default page.

```
$ curl http://192.168.56.11

<!DOCTYPE html>
....
```


## Uninstall Nginx

In order to allow us to see the full cycle we would like to check how to uninstall Nginx. This is the playbook we are going to use.

{% include file="examples/ansible/nginx_uninstall.yml" %}

Setting `state=absent` and running the playbook reported `changed=1` but the web server was still installed and running.
In order to fix that, first we need to stop the nginx service. That's what you see in the above playbook.


## Configure Nginx

It is not enough to install Nginx we also need to configure it. This involves a couple of steps.

1) Creating a configuration file.

{% include file="examples/ansible/static_site.cfg" %}

2) Putting it `/etc/nginx/sites-available/`.

3) Creating a symbolic link from `/etc/nginx/sites-enabled/` to that file.

4) Creating a directory where we put the pages of the website. For simplicity we are going to create a static web site. Without an application behind it. Just an HTML file and an image.

Locally they look like this:

```
static-site-src/
   index.html
   ansible-logo.jpg
```

{% include file="examples/ansible/static-site-src/index.html" %}

<img src="/img/ansible-logo.jpg" />

On the servers I'd like to put them in the `static-site` directory of user "foo".
That is in `/home/foo/static-site`.

5) Tell nginx to reload its configuration files.

## The Ansible Playbook to set up Nginx

{% include file="examples/ansible/nginx.yml" %}

Then I run this command:

```
$ ansible-playbook -i inventory.cfg  --limit 192.168.56.11 nginx.yml
```

Note, this time I have not supplied the `-b` flag to become root. Instead for each step where I wanted the command to be executed with `sudo` I've added the `become: yes` parameter.

The output looked like this:

```
PLAY [all] ******************************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [192.168.56.11]

TASK [ensure nginx is at the latest version] ********************************************************
changed: [192.168.56.11]

TASK [start nginx] **********************************************************************************
changed: [192.168.56.11]

TASK [copy the nginx config file and restart nginx] *************************************************
changed: [192.168.56.11]

TASK [create symlink] *******************************************************************************
changed: [192.168.56.11]

TASK [copy the content of the web site] *************************************************************
changed: [192.168.56.11]

TASK [restart nginx] ********************************************************************************
changed: [192.168.56.11]

PLAY RECAP ******************************************************************************************
192.168.56.11              : ok=7    changed=6    unreachable=0    failed=0
```

Then I could go ahead and check 

```
$ curl http://192.168.56.11
```

That printed:

```
<h1>Welcome to Ansible</h1>
<img src="/ansible-logo.jpg" />
```

When I visited the http://192.168.56.11/ from my desktop machine, it showed me the web page as I expected it, with the logo of Ansible.

## Comments

I got curl: (7) couldn't connect to host

<hr>

Hi,

I configured two EC2 RHL7 machine in AWS.(region - US East (Ohio))

1. control machine
2. Node machine

When i am trying to run playbook i get the below error.
------------------------------------------------
fatal: [172.31.18.198]: FAILED! => {"changed": false, "msg": "Repo rhui-REGION-client-config-server-7 forced skip_if_unavailable=True due to: /etc/pki/rhui/cdn.redhat.com-chain.crt\nRepo rhui-REGION-client-config-server-7 forced skip_if_unavailable=True due to: /etc/pki/rhui/product/rhui-client-config-server-7.crt\nRepo rhui-REGION-client-config-server-7 forced skip_if_unavailable=True due to: /etc/pki/rhui/rhui-client-config-server-7.key\nRepo rhui-REGION-rhel-server-releases forced skip_if_unavailable=True due to: /etc/pki/rhui/cdn.redhat.com-chain.crt\nRepo rhui-REGION-rhel-server-releases forced skip_if_unavailable=True due to: /etc/pki/rhui/product/content-rhel7.crt\nRepo rhui-REGION-rhel-server-releases forced skip_if_unavailable=True due to: /etc/pki/rhui/content-rhel7.key\nRepo rhui-REGION-rhel-server-rh-common forced skip_if_unavailable=True due to: /etc/pki/rhui/cdn.redhat.com-chain.crt\nRepo rhui-REGION-rhel-server-rh-common forced skip_if_unavailable=True due to: /etc/pki/rhui/product/content-rhel7.crt\nRepo rhui-REGION-rhel-server-rh-common forced skip_if_unavailable=True due to: /etc/pki/rhui/content-rhel7.key\n\n\nCould not contact any CDS load balancers: rhui2-cds01.us-east-2.aws.c..., rhui2-cds02.us-east-2.aws.c....\n", "rc": 1, "results": []}
-----------------------------

Could you please help me to understand the issue.

<hr>

I am trying to install nginx in node machine.

- hosts: webservers
tasks:
- name: ensure nginx is at the latest version
yum: name=nginx state=latest
- name: start nginx
service:
name: nginx
state: started

---

Enable ssh between the machines and mention the users: name your user here


