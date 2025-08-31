---
title: "Installing Perl and CPAN modules using Ansible"
timestamp: 2018-03-21T12:30:01
tags:
  - Ansible
  - Perl
published: true
author: szabgab
archive: true
---


For a Perl-based application you can either use the version of Perl that comes with the system or you can compile and install another version.

The same with modules from CPAN. You can use the versions that are in the package-management system of your Linux distribution, or you can install them directly from CPAN.

In this article we'll see how to use the system-perl and CPAN modules installed using `apt`.


## Ansible inventory file

{% include file="examples/ansible/inventory.cfg" %}

## Check version of Perl

```
$ ansible -i inventory.cfg 192.168.56.11 -a "perl -v"
192.168.56.11 | SUCCESS | rc=0 >>

This is perl 5, version 26, subversion 0 (v5.26.0) built for x86_64-linux-gnu-thread-multi
(with 56 registered patches, see perl -V for more detail)

Copyright 1987-2017, Larry Wall

Perl may be copied only under the terms of either the Artistic License or the
GNU General Public License, which may be found in the Perl 5 source kit.

Complete documentation for Perl, including FAQ lists, should be found on
this system using "man perl" or "perldoc perl".  If you have access to the
Internet, point your browser at http://www.perl.org/, the Perl Home Page.
```

Be less verbose. Print just the version number. Perl stores its version number
in the internal variable `$]`. We can print it on our command line using

```
$ perl -e 'print qq{$]\n}'

5.026000
```

Here I use the special quoting-style of Perl. Instead of double quotes `"$]\n"`
I used the [>qq](https://perlmaven.com/quoted-interpolated-and-escaped-strings-in-perl)
operator and the curly braces. This will make it easier to pass the whole
command as parameter to the Ansible command without the need of extensive escaping.

We can use the same code with Ansible to execute on the remote server(s).

```
$ ansible -i inventory.cfg 192.168.56.11 -a "perl -e 'print qq{$]\n}'"

192.168.56.11 | SUCCESS | rc=0 >>
5.026000
```

## Check version of specific Perl Module

Locally I can execute this code:

```
perl -mPath::Tiny -E 'say $Path::Tiny::VERSION'
```

Here I already use my knowledge about the version of Perl on the system. Knowing that perl is
at least version 5.10 I can use the `-E` flag and if I use that I can use the `say`
statement that automatically adds the `\n` to the end of the output.

The response however is a big blob of error.

```
$ perl -mPath::Tiny -E 'say $Path::Tiny::VERSION'
Can't locate Path/Tiny.pm in @INC (you may need to install the Path::Tiny module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.26.0 /usr/local/share/perl/5.26.0 /usr/lib/x86_64-linux-gnu/perl5/5.26 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.26 /usr/share/perl/5.26 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base).
BEGIN failed--compilation aborted.
```

In our case, as in most of the cases, the [Can't locate ... in @INC](https://perlmaven.com/cant-locate-in-inc) error just means we don't have [Path::Tiny](https://metacpan.org/pod/Path::Tiny) installed.

Let's see how does the same command work via Ansible?

```
$ ansible -i inventory.cfg 192.168.56.11 -a "perl -mPath::Tiny -E 'say $Path::Tiny::VERSION'"

192.168.56.11 | FAILED | rc=2 >>
Can't locate Path/Tiny.pm in @INC (you may need to install the Path::Tiny module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.26.0 /usr/local/share/perl/5.26.0 /usr/lib/x86_64-linux-gnu/perl5/5.26 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.26 /usr/share/perl/5.26 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base).
BEGIN failed--compilation aborted.non-zero return code
```


## Install Perl module sing apt

So far we ran our command on the remote server with the same username as we have locally. (foo in my case). User "foo" cannot install anything on its own. We either need to login to the remote server as user "root" or we need to use "sudo" on the remote server.

If we decide on the latter we can use the `-b` or `--become` flag that tells ansible it should "become another user" on the remote server. It defaults to become user `root` which is rather convenient.

```
ansible -i inventory.cfg 192.168.56.11 -m apt -a "name=libpath-tiny-perl state=present" -b
```

If you get an error with `"module_stdout": "sudo: a password is required\r\n",`, then
either you need to pass the `-K` parameter as well so Ansible will ask for the password of "foo" on the remote machine, or read and follow the article on [passwordless sudo](/enable-ansible-passwordless-sudo).

The output will be a bit verbose, but at the end we should have the module installed on our remote machine.

Let's check the version number again:


```
$ ansible -i inventory.cfg 192.168.56.11 -a "perl -mPath::Tiny -E 'say $Path::Tiny::VERSION'"

192.168.56.11 | SUCCESS | rc=0 >>
```

The response is successful, but we don't see the version number. I spent more than an hour figuring out that the problem was that the `$` sign in front of Path::Tiny was already interpreted by the local shell and thus the command did not arrive properly to the remote server. 

The solution is to escape the `$` using a back-slash:

```
ansible -i inventory.cfg all -a "perl -mPath::Tiny -E 'say \$Path::Tiny::VERSION'"

192.168.56.11 | SUCCESS | rc=0 >>
0.100
```

This way we can see that the version number of the Path::Tiny module is 0.100.


## Playbook to get Perl Module version number

We can also create a Playbook to retrieve the version of the Perl Module.
In the playbook we don't need to escape the `$` character,
by default Ansible will hide the output. So we need to add some extra statements
to the playbook to `register` the output of the command in arbitrary variable
we called `out`. Then need another step to print out the content in a debug message.

{% include file="examples/ansible/perl_module_version.yml" %}

This is the command to run the playbook:

```
ansible-playbook -i inventory.cfg --limit 192.168.56.11 perl_module_version.yml
```

This is the output from the playbook:

```
PLAY [all] ******************************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [192.168.56.11]

TASK [Module version] *******************************************************************************
changed: [192.168.56.11]

TASK [debug] ****************************************************************************************
ok: [192.168.56.11] => {
    "msg": "0.100"
}

PLAY RECAP ******************************************************************************************
192.168.56.11              : ok=3    changed=1    unreachable=0    failed=0
```


If we executed the same command on the other server, the one where we have not installed the module yet, we would get the nasty error we already know from the local execution of the command.

```
$ ansible-playbook -i inventory.cfg --limit 192.168.56.12 perl_module_version.yml

PLAY [all] ******************************************************************************************

TASK [Gathering Facts] ******************************************************************************
ok: [192.168.56.12]

TASK [Module version] *******************************************************************************
fatal: [192.168.56.12]: FAILED! => {"changed": true, "cmd": ["perl", "-mPath::Tiny", "-E", "say $Path::Tiny::VERSION"], "delta": "0:00:00.004247", "end": "2018-03-21 12:12:43.080453", "msg": "non-zero return code", "rc": 2, "start": "2018-03-21 12:12:43.076206", "stderr": "Can't locate Path/Tiny.pm in @INC (you may need to install the Path::Tiny module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.26.0 /usr/local/share/perl/5.26.0 /usr/lib/x86_64-linux-gnu/perl5/5.26 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.26 /usr/share/perl/5.26 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base).\nBEGIN failed--compilation aborted.", "stderr_lines": ["Can't locate Path/Tiny.pm in @INC (you may need to install the Path::Tiny module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.26.0 /usr/local/share/perl/5.26.0 /usr/lib/x86_64-linux-gnu/perl5/5.26 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl/5.26 /usr/share/perl/5.26 /usr/local/lib/site_perl /usr/lib/x86_64-linux-gnu/perl-base).", "BEGIN failed--compilation aborted."], "stdout": "", "stdout_lines": []}
	to retry, use: --limit @/home/foo/perl_module_version.retry

PLAY RECAP ******************************************************************************************
192.168.56.12              : ok=1    changed=0    unreachable=0    failed=1
```

