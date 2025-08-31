---
title: "Ansible playbook: print debugging statement"
timestamp: 2018-08-10T13:30:01
tags:
  - ansible-playbook
  - debug
  - msg
published: true
books:
  - ansible
author: szabgab
archive: true
---


A simple Ansible playbook example showing how to print debugging statements.


Create an Ansible Playbook file which is just a [YAML](/yaml) file:

{% include file="examples/ansible/debug_playbook.yml" %}

Run it as

```
$  ansible-playbook examples/ansible/debug_playbook.yml
```

The result will look like this:

```
 [WARNING]: Unable to parse /etc/ansible/hosts as an inventory source

 [WARNING]: No inventory was parsed, only implicit localhost is available

 [WARNING]: provided hosts list is empty, only localhost is available. Note that the implicit
localhost does not match 'all'


PLAY [Demo] *****************************************************************************************

TASK [debug] ****************************************************************************************
ok: [localhost] => {
    "msg": "Just echo something"
}

PLAY RECAP ******************************************************************************************
localhost                  : ok=1    changed=0    unreachable=0    failed=0
```


We run this on the local machine called `localhost`. It generates a few warnings, but we don't need an extra machine to play with.
If you'd like to eliminate these warnings you can create an inventory file that onlys lists localhost:

{% include file="examples/ansible/localhost.cfg" %}

And supply it on the command line:

```
$  ansible-playbook -i examples/ansible/localhost.cfg  examples/ansible/debug_playbook.yml
```


## Incorrect indentation: Ignoring invalid attribute: msg

One thing you need to be aware is that YAML derives its structure from the indentations and thus you need to make sure the `msg` tag is indented properly. If the indentation is incorrect as in the next example:

{% include file="examples/ansible/debug_playbook_bad.yml" %}

Then running it:

```
$  ansible-playbook -i examples/ansible/localhost.cfg  examples/ansible/debug_playbook_bad.yml
```

will yield the following output including the warning:

```
 [WARNING]: Ignoring invalid attribute: msg


PLAY [Demo] *****************************************************************************************

TASK [debug] ****************************************************************************************
ok: [127.0.0.1] => {
    "msg": "Hello world!"
}

PLAY RECAP ******************************************************************************************
127.0.0.1                  : ok=1    changed=0    unreachable=0    failed=0
```


## No name

Finally, just to make anothe small change, one does not need to provide the `name` field at all:

{% include file="examples/ansible/debug_playbook_noname.yml" %}

Result:

```
$  ansible-playbook -i examples/ansible/localhost.cfg  examples/ansible/debug_playbook_noname.yml
```

```

PLAY [localhost] ************************************************************************************

TASK [debug] ****************************************************************************************
ok: [127.0.0.1] => {
    "msg": "Just echo something"
}

PLAY RECAP ******************************************************************************************
127.0.0.1                  : ok=1    changed=0    unreachable=0    failed=0

```


## Print results of shell commands

{% include file="examples/ansible/debug_playbook_shell.yml" %}

