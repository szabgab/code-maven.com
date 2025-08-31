---
title: "Ansible - localhost"
timestamp: 2021-03-16T11:30:01
tags:
  - Ansible
description: "Experiment with Ansible on localhost"
published: true
books:
  - ansible
author: szabgab
archive: true
show_related: true
---


Experiment with Ansible on localhost


## Prepare a YAML-based inventory file

{% include file="examples/ansible/localhost/inventory.yml" %}

## Create an Ansible configuration file

Telling Ansible where the inventory is.

{% include file="examples/ansible/localhost/ansible.cfg" %}

Make sure you can ssh to localhost:

```
cd ~/.ssh
cat id_rsa.pub >> authorized_keys
```

Then you can start running commands:

```
ansible all -m ping
ansible all -m ping
```



