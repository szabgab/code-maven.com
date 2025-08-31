---
title: "Generate and deploy ssh private public keypair (ssh-keygen, ssh-copy-id)"
timestamp: 2018-03-06T14:30:01
tags:
  - ssh
  - ssh-keygen
  - ssh-copy-id
  - id_rsa
published: true
author: szabgab
archive: true
---


In order to be able to automatically log in to another computer without the need to provide a password,
the most common solution is to generate an ssh keypair, a private and a public key on the machine from which
we initiate the connection. Copy the public key over to the hosts to which we would like to log in to.

Set the file ownership rights properly.


## Generate the ssh keypair

Run the `ssh-keygen` program on the command line and press ENTER on every question:

```
$ ssh-keygen
```

More or less this is the expected output: (assuming your username is `foo` and
your home directory is `/home/foo`.)

```
Generating public/private rsa key pair.
Enter file in which to save the key (/home/foo/.ssh/id_rsa):
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
Your identification has been saved in /home/foo/.ssh/id_rsa.
Your public key has been saved in /home/foo/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:CL+xpn2DJx4P3xddsCWAN2thkFIHKFp9kBr6NHf44Pw foo@ubuntu-ansible
The key's randomart image is:
+---[RSA 2048]----+
|       ..=+=o.   |
|      + = +.= o .|
|    .+ + + o + = |
|    oo+.+ . o . .|
|     o+=S+ . . . |
|      .+o . . .  |
|      *. .   .   |
|     +o=+.E .    |
|    ..o+o...     |
+----[SHA256]-----+
```


This generates two files: `~/.ssh/id_rsa` is the private key. You need to keep it super-safe.
`~/.ssh/id_rsa.pub` is the public key. This you can distribute to anyone. You can even advertise it
on your site. One, theoretically, cannot compute the private key based on the public key in any reasonable time.

## Deploy the public key

Basically you need to take the content of `~/.ssh/id_rsa.pub` on the manager machine and
append it to the content of `~/.ssh/authorized_keys` and make sure both the `~/.ssh` directory
and the `~/.ssh/authorized_keys` file has very restricted rights allocated:

```
drwx------ 2 foo foo ... .ssh/
-rw------- 1 foo foo ... .ssh/authorized_keys
```

Luckily you don't need to do it manually as there is a command called `ssh-copy-id` that will do all of that
on your behalf. Of course it will ask you to type in the password of the remote machine as it needs to log-in once
before it copied the public key, but then it creates the necessary directory and file if necessary and appends the
new public key. We just need to provide the IP address of the remote server.

```
ssh-copy-id 192.168.56.11
```

The output looks like this:

```
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/foo/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
foo@192.168.56.11's password:

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh '192.168.56.11'"
and check to make sure that only the key(s) you wanted were added.
```

Then you can `ssh` to the remote machine without providing a password.

```
$ ssh 192.168.56.11
```

