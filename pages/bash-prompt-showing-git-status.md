---
title: "Bash prompt showing git status"
timestamp: 2021-06-21T09:30:01
tags:
  - Bash
  - PS1
published: true
books:
  - shell
author: szabgab
archive: true
show_related: true
---


This code snippet can be included un the ~/.bash_profile It will change the Linux shell prompt
to indicate the name of the current branch (if the current working directory is inside a git repository).
It will also use color-code to indicate if there are non-committed files in the current repository.

Red for when there are non-committed files, yellow when everything is committed, but some changes have not been pushed to remote yet,
and green when the directory is clean.

Of course it works on the current branch so if you have unpushed commits in other branches this won't indicate it.


{% include file="examples/bash_git_prompt.sh" %}

Feel free to reuse any part of this code.
