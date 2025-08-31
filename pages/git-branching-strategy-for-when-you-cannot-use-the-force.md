---
title: "git branching strategy for when you cannot use the --force"
timestamp: 2021-09-29T11:30:01
tags:
  - git
  - rebase
  - force
published: true
books:
  - git
author: szabgab
archive: true
show_related: true
---


One nice thing about the way git works is that I can update my feature development branch from the main development branch whatever it is called, without a trail of merges. We can use rebase
to pretend we have started our branch using the most up-to-date version of the main development branch. In such case, if we have already pushed out our branch to a remote repository we' will
have to use the --force to push out the version of our branch.

This can be done safely if there is only a single person working on such branch and if everyone looking at that branch is aware that this might happen.

However there are certain situations when this technique cannot be used. For example if repository syncing is set up (e.g. between BitBucket and GitLab) then a push --force will stop the syncing of that branch.

My solution for this situation is to create a new branch based on the first one. e.g.



```
git checkout -b feature_a_v1
```

work, push to this branch

In the meantime the main development branch, let's call it 'dev' moved ahead. This is what I'll do:

```
# update the local version of dev
git checkout dev
git pull
```


```
# go to my branch and create a new branch based on this:
git checkout  feature_a_v1
git checkout  -b feature_a_v2
```


```
# Now on feature_a_v2 rebase the dev branch and then push it out
git rebase dev
git push --set-upstream origin feature_a_v2
```

```
# remove the old branch both locally and from the server
git branch -d feature_a_v1
git push origin --delete feature_a_v1
```


Alternative: remove the remote branch (but that probably will not remote the branch from the synced version) and add it again. (this might not work)

Alternative: just add a new remote branch and remove the old one. No need to have a new local branch.

