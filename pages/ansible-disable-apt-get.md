---
title: "Stop and disable apt-get using Ansible"
timestamp: 2019-03-26T07:30:01
tags:
  - apt-get
  - Ansible
published: true
books:
  - ansible
author: szabgab
archive: true
---


Disable the apt services to avoid collision between the `apt-get update` that runs when we start a new instance
and the Ansible process that tries to install modules:

The first one stops the service right now.

The second is there so when the service won't even start next time we boot or computer.

```
- name: Stop services
  service:
    name: "{{ item }}"
    state: stopped
  with_items:
    - apt-daily
    - apt-daily.timer
    - apt-daily-upgrade
    - apt-daily-upgrade.timer

- name: Disable services
  service:
    name: "{{ item }}"
    enabled: no
  with_items:
    - apt-daily
    - apt-daily.timer
    - apt-daily-upgrade
    - apt-daily-upgrade.timer
```

