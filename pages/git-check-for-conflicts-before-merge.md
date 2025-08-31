---
title: "Git: Check for conflicts before merge"
timestamp: 2019-06-26T21:30:01
tags:
  - git
published: true
author: szabgab
archive: true
---


How can we check if a merge is going to create a conflict or not without actually doing the merge.

Apparently there is no single command for this, but it is easy to do:


```
git merge --no-commit --no-ff BRANCH-TO-MERGE
echo $?
git merge --abort
```

The first command will try to merge, but without committing the change and without fast-forwarding.

This command will succeed if the merge can be executed and it will fail if there is a conflict.
So we can check if the exit code `$?` was 0 (success) of non-zeo (failure).
Then we have to clean up the partial merge.


## Sequence to demonstrate

{% include file="examples/check_for_conflict.sh" %}

