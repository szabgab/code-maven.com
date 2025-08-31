---
title: "Waiting with Ansible, pausing a Playbook"
timestamp: 2018-03-18T19:00:01
tags:
  - Ansible
  - pause
published: true
books:
  - ansible
author: szabgab
archive: true
---


Sometimes we need to wait some time before we can let our Ansible process to continue.


This playbook will show the current time on the server. Wait 3 second and then show the time again.

{% include file="examples/ansible/sleep.yml" %}

The output looks like this:

```
i$ ansible-playbook -i inventory.cfg --limit 192.168.56.11 -b sleep.yml

PLAY [all] ****************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************
ok: [192.168.56.11]

TASK [check date] *********************************************************************************************************************
changed: [192.168.56.11]

TASK [debug] **************************************************************************************************************************
ok: [192.168.56.11] => {
    "msg": "Sun Mar 18 18:35:59 IST 2018"
}

TASK [pause] **************************************************************************************************************************
Pausing for 3 seconds
(ctrl+C then 'C' = continue early, ctrl+C then 'A' = abort)
ok: [192.168.56.11]

TASK [check date] *********************************************************************************************************************
changed: [192.168.56.11]

TASK [debug] **************************************************************************************************************************
ok: [192.168.56.11] => {
    "msg": "Sun Mar 18 18:36:02 IST 2018"
}

PLAY RECAP ****************************************************************************************************************************
192.168.56.11              : ok=6    changed=2    unreachable=0    failed=0
```

Read more about [pause](http://docs.ansible.com/ansible/latest/pause_module.html).
