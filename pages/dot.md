---
title: "dot file or configuration files"
timestamp: 2019-02-03T07:30:01
tags:
  - CodeMaven
published: true
author: szabgab
archive: true
---


When setting up a new account on a Linux machine there are many things one can configure.
This is a collection of the "dot files", (the ones that usually start with a dot and therefore are hidden)
that I use.


* [tmux](/tmux)
* [git config](/git-config) ([Enforcing commit message format in Git - on the client side](/enforcing-commit-message-format-in-git))

## Bash

<pre>
alias xssh='ssh -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
alias myscp='scp -q -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no'
alias rm='rm -i'
alias mv='mv -i'
alias cp='cp -i'
alias ll='ls -l'
alias l='ls -la'
export HISTSIZE=1000
export EDITOR=vim
```

Make bash write to the `.bash_history` file immediately and read it on every command.
Allowing you to search and use the history created in one terminal to be used in another terminal.

```
shopt -s histappend
export PROMPT_COMMAND="history -a; history -c; history -r;"
</pre>

## ssh config

```
Host 10.* 172.31.* 172.32.* 172.33.* 172.34.*
   StrictHostKeyChecking no
   UserKnownHostsFile /dev/null
```

in ~/.ssh/config


