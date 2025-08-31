---
title: "Per project (per directory) private ssh keys for git"
timestamp: 2018-07-03T16:30:01
tags:
  - git
  - ssh
  - ssh-keygen
published: true
books:
  - git
author: szabgab
archive: true
---


I wanted to show how two people with two separate accounts on GitHub, Bitbucket, or GitLab can work in a cooperation.
For this I had to make sure that when I interact with the remote server I use it with the correct account.


In order to log in to the same server (e.g. GitHub) with two different accounts I use two browsers. For user A I use Firefox.
For user B I use Chrome.

For `push` and `pull` it was a bit trickier. I think I could have used `https` access, but that would mean for every interaction I have to type in my password. I wanted to avoid that. So I wanted to use ssh access.

So I will need a separate set of ssh-keypairs for each user and I'll need to set up some configuration that will always use the correct keypair.

`ssh` allows the use of a configuration file located in `~/.ssh/config` that allows us to configure different keypairs (identity files) per host. This is how an entry in that file looks like:

```
host github.com
   HostName github.com
   IdentityFile ~/.ssh/id_rsa
   User szabgab
```

This however does not help us as this is based on the target hostname and I'd like to access the same host, and even use the same remote username (git) but use two different Identity files.

## The solution

Generate new Identity files:

```
mkdir id_a
ssh-keygen -f id_a/id_rsa -N ''
```

The `-N ''` will tell the command to use an empty passphrase. The `-f id_a/id_rsa` tells the command where to save the new Identity file. The Public key will be saved next to it with .pub extension.

We can then take the public key and upload it to our cloud-based Git server to the account of user "A".

We do the same with user "B".


The next command will configure git to use the ssh command passing it the path of the identity file of A.
Basically the first command will changes the file `~/.gitconfig` adding

```
[core]
    sshCommand = "ssh -i /full/path/to/id_a/id_rsa"
```

The `clone` command will use this `ssh` and finally we remove the entry from the global configuration file.

```
git config --global core.sshCommand "ssh -i /full/path/to/id_a/id_rsa"
git clone ...
git config --global --unset core.sshCommand
```

Configure each cloned directory to use its own identity file and its own user and email for
the identification of commits.

```
cd project-dir
git config --local core.sshCommand "ssh -i /full/path/to/id_a/id_rsa"
git config --local user.name "User A"
git config --local user.email A@code-maven.com
```

This will change the `.git/config` file in the current directory.

## Full steps

Let's assume we have two Bitbucket users: Mary and Joe with usernames "mary" and "joe" respectively.
Mary has a private repository called  `https://bitbucket.org/mart/demo`.
She configures it to make it writable by Joe as well. (Done on the web interface of BitBucket.)

We create directory to use for this whole project:

```
cd ~
mkdir demo
cd demo
```

We create directories for the identity files:

```
mkdir mary
mkdir joe
```

We generate two Identity Files:

```
ssh-keygen -f mary/id_rsa -N ''
ssh-keygen -f joe/id_rsa -N ''
```

We upload the content of `mary/id_rsa.pub` to the BitBucket account of Mary and the
content of `joe/id_rsa.pub` to the BitBucket account of Joe.

We clone the repository of Mary with the credentials of Mary to the local directory called "demo_mary"
but we also make sure to remove her credentials from the global configuration file.

```
git config --global core.sshCommand "ssh -i mary/id_rsa"
git clone git@bitbucket.org:mary/demo.git demo_mary
git config --global --unset core.sshCommand
```

Then we configure this newly cloned repository to use the credentials of Mary:

```
cd demo_mary
git config --local core.sshCommand "ssh -i mary/id_rsa"
git config --local user.name "Mary"
git config --local user.email mary@code-maven.com
```

Then we go back to the common directory and do the same for Joe:

We clone the repository of Mary using the credentials of Joe and then remove
those credentials from the global configuration file:

```
cd ..
git config --global core.sshCommand "ssh -i joe/id_rsa"
git clone git@bitbucket.org:mary/demo.git demo_joe
git config --global --unset core.sshCommand
```

Then we configure this newly cloned repository to use the credentials of Joe:

```
cd demo_joe
git config --local core.sshCommand "ssh -i joe/id_rsa"
git config --local user.name "Joe"
git config --local user.email joe@code-maven.com
```

## The short solution

```
GIT_SSH_COMMAND="ssh -i /full/path/to/id_a/id_rsa" git clone ...
cd repo_name
git config --local core.sshCommand "ssh -i /full/path/to/id_a/id_rsa"
git config --local user.name "User A"
git config --local user.email A@code-maven.com
```

