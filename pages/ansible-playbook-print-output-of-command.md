---
title: "Ansible playbook: print output of command"
timestamp: 2018-08-16T15:30:01
tags:
  - ansible-playbook
  - uptime
  - ssh
published: true
books:
  - ansible
author: szabgab
archive: true
---


An old example that might or might not work.



## Setup

For this example we are using an inventory file that only lists localhost:

{% include file="examples/ansible/localhost.cfg" %}

Unlike the sime <a href="">debug printing</a> example, this will require ssh access to the target machine, which is the same machibe we are working on. You still need to make sure you can `ssh` to `localost` without any password.


`

{% include file="examples/ansible/output_playbook.yml" %}


```
$  ansible-playbook -i examples/ansible/localhost.cfg examples/ansible/output_playbook.yml
```


```
PLAY [localhost] ************************************************************************************

TASK [debug] ****************************************************************************************
ok: [127.0.0.1] => {
    "msg": "Debug statement"
}

TASK [shell] ****************************************************************************************
changed: [127.0.0.1]

TASK [debug] ****************************************************************************************
ok: [127.0.0.1] => {
    "result": {
        "changed": true,
        "cmd": "/usr/bin/uptime",
        "delta": "0:00:00.011499",
        "end": "2018-08-10 13:52:34.651618",
        "failed": false,
        "rc": 0,
        "start": "2018-08-10 13:52:34.640119",
        "stderr": "",
        "stderr_lines": [],
        "stdout": "13:52  up 13 days,  6:01, 4 users, load averages: 1.42 1.88 1.91",
        "stdout_lines": [
            "13:52  up 13 days,  6:01, 4 users, load averages: 1.42 1.88 1.91"
        ]
    }
}

PLAY RECAP ******************************************************************************************
127.0.0.1                  : ok=3    changed=1    unreachable=0    failed=0

```

