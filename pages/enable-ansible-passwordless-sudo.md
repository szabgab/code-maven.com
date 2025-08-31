---
title: "Enable passwordless sudo for ansible"
timestamp: 2018-03-14T19:30:01
tags:
  - Ansible
  - sudo
  - visudo
published: true
books:
  - ansible
author: szabgab
archive: true
---


In order to fully control a remote machine we need to be able to execute command on the remote machines as user `root`.
There are a number of ways to accomplish this. Each one with a slightly different security implication.


## Some of our options to execute commands as root

We can log in to the remote server as user `root` providing password on each login.

We can log in to the remote server as user `root` using ssh keys.

We can login as an unprivileged user and then use `sudo` after providing the password of the user.

We can login as an unprivileged user and then use `sudo` without providing a password.

We'll try he last two now.

Our inventory.cfg looks like this:

```
[all]
192.168.56.11
192.168.56.12

[all:vars]
ansible_python_interpreter=/usr/bin/python3
```

We are running on our manager machine as user `foo` and we are accessing the remote machine as user `foo`.

Let's check if we can use Ansible at all.

```
$ ansible -i inventory.cfg all -m ping
```

```
192.168.56.11 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
192.168.56.12 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```

## grep ^root: /etc/shadow

This is not  very sophisticated or useful command. We just want to display the information about user `root` in the `/etch/shadow` file using `grep`. The point is, that only user `root` has the rights to do this.

```
$ ansible -i inventory.cfg all -a "grep ^root: /etc/shadow"
```

It fails as expected:

```
192.168.56.12 | FAILED | rc=2 >>
grep: /etc/shadow: Permission deniednon-zero return code

192.168.56.11 | FAILED | rc=2 >>
grep: /etc/shadow: Permission deniednon-zero return code
```

Only user `root` can read the `/etc/shadow` file.

## Become user root

Adding the `-b` or `--become` flag tells Ansible to `become another user` on the remote server.
The "other" can be configured, but defaults to `root` which is rather convenient.

```
$ ansible -i inventory.cfg all -a "grep ^root: /etc/shadow"  -b
```

It fails now in a different way. It tries to use `sudo` but fails because `sudo` needs a password.

```
192.168.56.12 | FAILED! => {
    "changed": false,
    "module_stderr": "Shared connection to 192.168.56.12 closed.\r\n",
    "module_stdout": "sudo: a password is required\r\n",
    "msg": "MODULE FAILURE",
    "rc": 1
}
192.168.56.11 | FAILED! => {
    "changed": false,
    "module_stderr": "Shared connection to 192.168.56.11 closed.\r\n",
    "module_stdout": "sudo: a password is required\r\n",
    "msg": "MODULE FAILURE",
    "rc": 1
}
```

## Prompt for password

We can use the `-K` or `--ask-become-pass` flag to tell Ansible to ask for the sudo password.

```
$ ansible -i inventory.cfg all -a "grep ^root: /etc/shadow"  -b -K
```

It asks for the SUDO password and then uses that on both machines. I guess if the passwords were different on the two machines then it will notice this and ask for the other password as well. I have never tried that.

```
SUDO password:
192.168.56.11 | SUCCESS | rc=0 >>
root:!:17596:0:99999:7:::

192.168.56.12 | SUCCESS | rc=0 >>
root:!:17596:0:99999:7:::
```


## Allow passwordless sudo

Telling ansible ask for the password has the security advantage that only people who know what is the password can execute code
but it can be a bit inconvenient on the long run.

Instead we can configure the the remote user we use to be able to execute all, or certain commands using `sudo` even without supplying a password. In this case we need to protect the user account of the manager machine that has its public ssh-key installed on the remote server. Anyone who can access this machine would be able to control the remote servers.

Who can run `sudo` command, what are theses command and whether password is required is controlled in the `/etc/suduers` file. It can be edited manually using the `visudo` command or we can ask Ansible to edit it. You can also edit the file with any editor, but if you save an incorrectly formatted version, you can easily lock yourself out from user root. Hence it is strongly recommended that you use the `visudo` command that will validate the syntax of the file before you save it.

<h3>Manually editing the sudoers</h3>

`ssh` to the remote server.

```
$ ssh foo@192.168.56.11
```

On the remote server run:

```
$ sudo visudo
```

It will ask for your password and then open the default editor which happens to be [nano](/nano) these days.
The default version of file looks like this:

```
#
# This file MUST be edited with the 'visudo' command as root.
#
# Please consider adding local content in /etc/sudoers.d/ instead of
# directly modifying this file.
#
# See the man page for details on how to write a sudoers file.
#
Defaults	env_reset
Defaults	mail_badpass
Defaults	secure_path="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

# Host alias specification

# User alias specification

# Cmnd alias specification

# User privilege specification
root	ALL=(ALL:ALL) ALL

# Members of the admin group may gain root privileges
%admin ALL=(ALL) ALL

# Allow members of group sudo to execute any command
%sudo	ALL=(ALL:ALL) ALL

# See sudoers(5) for more information on "#include" directives:

#includedir /etc/sudoers.d
```

We need to edit the line

```
%sudo   ALL=(ALL:ALL) ALL
```

and look like this:

```
%sudo  ALL=(ALL:ALL) NOPASSWD: ALL
```

We can save the file and exit.

In order to verify that it works properly log out from the server (e.g. type `exit` or press `Ctrl-d`.
Then ssh to the server again and run

```
sudo grep root /etc/shadow
```

We needed to logout and login again for the verification because normally even if sudo requires a password it retains the access rights for a few minutes or until you log out. So we wanted to make sure we can use `sudo` because of the change in the `sudoers` file and not because of this grace period.

We can now log out again and on the management machine run the ansible command again with `-b` but without `-K`

```
$ ansible -i inventory.cfg all -a "grep ^root: /etc/shadow"  -b
```

The result looks promising:

```
192.168.56.12 | FAILED! => {
    "changed": false,
    "module_stderr": "Shared connection to 192.168.56.12 closed.\r\n",
    "module_stdout": "sudo: a password is required\r\n",
    "msg": "MODULE FAILURE",
    "rc": 1
}
192.168.56.11 | SUCCESS | rc=0 >>
root:!:17596:0:99999:7:::
```

One machine where we changed the `sudoers` file worked as expected, the other one without the passwordless access
failed as expected.

(We could use the `-K` and then it would ask for a password again, but instead of that we'd like to allow passwordless
`sudo` commands on the other machine as well.


## Ansible playbook to set passwordless sudo

This is the `set_sudoer.yml` file.

```
---
- hosts: all
  tasks:
    - lineinfile:
        path: /etc/sudoers
        state: present
        regexp: '^%sudo'
        line: '%sudo ALL=(ALL) NOPASSWD: ALL'
        validate: 'visudo -cf %s'
```

It says: work on the file in the given `path`.
Replace the line matched by `regexp` with the string in `line`.
Before saving the file run the `validate` command to verify that format is correct.

It will match the following line:

```
%sudo   ALL=(ALL:ALL) ALL
```

and replace it with this line:

```
%sudo  ALL=(ALL:ALL) NOPASSWD: ALL
```

We can run this with the following command:

```
$ ansible-playbook -i inventory.cfg --limit 192.168.56.12 set_sudoer.yml -b -K
```

* We only run it on the selected host.
* We provide the `-b` as we need to become `root` for this operation.
* We also supply `-K` because sudo still requires password.

The output looks like this:

```
SUDO password:

PLAY [all] ****************************************************************************************************************************

TASK [Gathering Facts] ****************************************************************************************************************
ok: [192.168.56.12]

TASK [lineinfile] *********************************************************************************************************************
changed: [192.168.56.12]

PLAY RECAP ****************************************************************************************************************************
192.168.56.12              : ok=2    changed=1    unreachable=0    failed=0
```

Once this is done, we can run the previous command without providing a password and it will run on both servers:

```
$ ansible -i inventory.cfg all -a "grep ^root: /etc/shadow"  -b
```

```
192.168.56.12 | SUCCESS | rc=0 >>
root:!:17596:0:99999:7:::

192.168.56.11 | SUCCESS | rc=0 >>
root:!:17596:0:99999:7:::
```

## Conclusion

Having passwordless access is great for automation, but you need to be aware of the security implications we discussed above.

## Comments

This enables passwordless sudo for all accounts for all commands.

Surely it would be better to follow the recommendation in the /etc/sudoers file and use the lineinfile module to create a file, say, /etc/sudoers.d/ansible containing a line something like (untested)

foo ALL = (root:root) NOPASSWD: ALL


---

I tried this, using 'ansible' instead of 'foo', but Ansible would still says it required a password. I had also made the 'ansible' user usable by *my* username without password, by using:

```
- name: Get the username running the deploy
local_action: command whoami
register: username
become: false

- name: Allow using this user without password
lineinfile:
dest: /etc/sudoers.d/ansible
state: present
regexp: "^{{ username.stdout }}"
line: "{{ username.stdout }} ALL=(ansible) NOPASSWD: ALL"
validate: 'visudo -cf %s'
```

Works on the command line, not in Ansible...

---

%sudo ALL=(ALL:ALL) NOPASSWD: ALL

should be

%sudo ALL=(ALL:ALL) NOPASSWD:ALL

If you're not careful, that extra space just after `NOPASSWD:` will ruin your system like it did mine (even when using visudo which was unexpected)


