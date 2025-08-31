---
title: "Enforce fast forward as merge strategy in Git"
timestamp: 2018-08-15T22:30:01
tags:
  - git
published: true
author: szabgab
archive: true
---


Some people like to see lots of branches and the way they are merged together in their git history. Others like to have nice straight line.

Some companies have a development workflow in which the only way to add to the "master" branch is to send a pull-request, get it reviewed, approved and then merged into "master". For them it might be useful to enforce that merging into master can be done only with a fast-forward merge.


There are several ways to enforce it or at least to gently nudge you in the chosen direction.

[Aaron Bonner](https://twitter.com/ajbonner) wanted to
[Only Allow Git Fast-forward Merges to Avoid Ugly Merge Commits](https://aaronbonner.io/post/78444674979/only-allow-git-fast-forward-merges-to-avoid-ugly) and he suggested execute

```
git config --global merge.ff only
```

That will add an entry to your `~/.gitconfig` file:

```
[merge]
    ff = only
```

and it will require that you only merge branches that can fast-forward. That basically forces you to either rebase before merging, or turn off this configuration, or to force your way through using

```
git merge --no-ff
```

Alternatively you can execute the following command <b>while inside a git workspace</b>

```
git config --local merge.ff only
```

This will add the same entry to the `.git/config` of the current project.
This way the enforcing only happens in specific projects.

Of course all this is on the client side and not on the server.

## Enforce fast-forward to a single branch only

Adding the following to the `.git/config` file of your project will enforce the "merge only with fast-forward" rule on the "master" branch only.

```
[branch "master"]
    mergeOptions = --ff-only
```

This is also describe by [Marko Vuksanovic](https://twitter.com/mvuksano) 
in [Git tips: Use only fast-forward merges (with rebase)](https://medium.com/@mvuksano/git-tips-use-only-fast-forward-merges-with-rebase-c80c9d260a83)

## Team Foundation Server

TFS allows the admins to set 
[branch policies](https://docs.microsoft.com/en-us/vsts/repos/git/branch-policies?view=vst). Among the several features one can <b>Enforce a merge strategy</b>, but as far as I can see only <b>No fast-forward merge</b> and <b>Squash merge</b> are available.


## Atlassian BitBucket

The documentation seems to indicated that the admin of a project can set the
[available merge strategies](https://confluence.atlassian.com/bitbucketserver/pull-request-merge-strategies-844499235.html), but all I managed to do was to set the default merge strategy. It indeed stopped me from accepting a pull-request that could not be merged using fast-forward. However I was still able to pick a different merge strategy when I was about to accept the pull-request.

Maybe I have not looked close enough.

## GitHub

As far as I know GitHub does not support requiring fast-forward when you accept and [merge a pull-request](https://help.github.com/articles/merging-a-pull-request/).

## GitLab

As I can see one can set [fast forward merge](https://docs.gitlab.com/ee/user/project/merge_requests/fast_forward_merge.html) as the only acceptable merge strategy.


## Comments

On Bitbucket Server you can install my "Control Freak" plugin to enforce a fast-forward policy when merging into certain branches (e.g., master).

