---
title: "Reboot using Ansible"
timestamp: 2018-03-18T17:00:01
tags:
  - Ansible
published: true
books:
  - ansible
author: szabgab
archive: true
---


Sometime we need to reboot the servers using Ansible


## Ad-hoc command to reboot a single server

```
$ ansible -i inventory.cfg  192.168.56.11 -b -a "/sbin/shutdown -r now"
```

This reboots the server, but the reboot starts before Ansible finishes its work and thus it gives the following error message.

```
192.168.56.11 | UNREACHABLE! => {
    "changed": false,
    "msg": "Failed to connect to the host via ssh: Shared connection to 192.168.56.11 closed.\r\n",
    "unreachable": true
}
```


## Ad-hoc command for delayed reboot

We can tell the `shudown` command to wait 1 minute (or more) and reboot only after that. (Probably 1-2 sec would be enought but as far as I know you cannot specify that for the `shutdown command`.) This gives enough time for Ansible to return a success report. It returns immediately and the machine shuts down (and because of the `-r` flag reboots) 1 minutes later.

```
$ ansible -i inventory.cfg  192.168.56.11 -b -a "/sbin/shutdown -r +1"
```

```
192.168.56.11 | SUCCESS | rc=0 >>
Shutdown scheduled for Sun 2018-03-18 17:01:40 IST, use 'shutdown -c' to cancel.
```

## Reboot in a playbook

```
---
- hosts: all
  tasks:
     - command: /sbin/shutdown -r now
```

```
---
- hosts: all
  tasks:
     - name: reboot
      command: /sbin/shutdown -r now
```

```
ansible-playbook -i inventory.cfg --limit 192.168.56.11 -b reboot.yml
```

This was also discussed in the [Getting started with Ansible on CentOS](/getting-started-with-ansible-centos) article.

## Forgetting to become root

With all the explanation, the next time I tried to reboot a server I forgot to tell Ansible to <b>become root</b>.
Or in other words, I've forgotten to supply the `-b` flag.

```
$ ansible -i inventory.cfg 192.168.56.11 -a "/sbin/shutdown -r now"
```

The response was violent.

```
192.168.56.11 | FAILED | rc=1 >>
Failed to set wall message, ignoring: Interactive authentication required.
Failed to reboot system via logind: Interactive authentication required.
Failed to open /dev/initctl: Permission denied
Failed to talk to init daemon.non-zero return code
```

It took me a while to understand what happened, but afer a while I figure it out:

```
$ ansible -i inventory.cfg 192.168.56.11 -a "/sbin/shutdown -r now -b"
```

## Comments


Gabor, you have a typo in last command.
the -b should be outside the " "

---

Thank you for sharing :D This helped me with my jenkins job where I wanted to avoid the unreachable error because I was shutting down a machine.

<h2>

reboot starts before Ansible finishes its work ... see: https://stackoverflow.com/questions/29955605/how-to-reboot-centos-7-with-ansible
for async goodness. Also https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_async.html



