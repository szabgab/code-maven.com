---
title: "Git Workflow for teams using a single remote repository"
timestamp: 2018-06-30T11:30:01
tags:
  - git
published: true
books:
  - git
author: szabgab
archive: true
---


Once you know what interesting [workflows are there for individuals](/git-workflow-for-individuals) you can start
thinking about the workflow for your team. Let's see our options using a single remote repository.


## Centralized workflow - single master

In the centralized workflow we use a single repository on the server and a single branch called "master". Everyone clones the
central git repository. Everyone makes local changes on the "master" branch.
When a developer wants to push out the changes to the server two things can happen. If the server was not updated since this developer cloned the repository or since she pushed to it the last time, then this new "git push" will work.

If however there are changes on the server that are not yet present in the local git repository of the developer then first she needs to bring them to her computer. This can be done using `git pull` that will result in a local merge, or it can be done using
`git pull --rebase` that will rebase the local change on top of the changes that come from the remote server.

In either case, after the `pull` the developer can now `push` oit her changes. (Assuming noone has updated the remote server since the `pull`.)

A huge advantage is that this workflow is very simple to learn, but we have to think about speed of progress and code stability.

We can have two approaches. We can demand "master" to be always in a releasable state or we can allow the developers to mess it up and then have "code freeze" before each release.

In the "master is stable" approach people have to be very careful about the changes they make as to not break "master".
If the code in "master" gets broken (e.g. it does not compile, does not pass tests) that will impact the work of every developer and break the promise. This apprach means that at every time, even when we are in the middle of implementing a feature we need to be able to release the code. We might use <b>feature flags</b> to hide the not yet fully developed feature from the real users.

The "allow masrer to be a mess" approach is different. In this case every time we want to release a new version we would declare a "code freeze" in which only bug-fixes relevant to the upcoming release are allowed to be pushed to the central repository. Sometimes these "code freezes" take several weeks. During this time many of the developers are stuck. They cannot push new code to the central repository. So even if they make changes locally they cannot properly cooperate with other developers.

The latter approach usually creates a lot of downtime and a lot of frustration.

## Single remote - feature branches

In this workflow we still use a single remote server, but this time we use feature-branches to develop code.
We keep "master" always in a releasable state. For every feature, for every bug-fix we create a separate branch.
Unlike in the single developer mode however, here we will most likely push out the feature-branch to the central
repository to allow cooperation with others.


Start from the master branch:

```
$ git checkout master
```

Create a feature branch locally and switch to it: (could have been one command `git checkout -b feature`)

```
$ git branch feature
$ git checkout feature
```

Make some local changes:

```
$ git add .
$ git commit -m "message"
```

Push out the branch and set up the local branch to be mapped to the remote branch.

```
$ git push -u origin feature
```

Other developers can now start working on this branch. For this they need to do the following:

In a clean workspace switch to the "master" branch and pull everything from the remote server.

```
$ git checkout master
$ git pull
```

Set up the local branch following the remote feature branch:

```
$ git branch feature origin/feature
```

From this point on the "feature" branch can be used by both developers. They can simply "push" their local changes to
the remote branch  and "pull" from the remote server the changes done by the other developers. If for the `pull`
command we also use the `--rebase` flag then the history on this branch will be a nice straight line just as the
individual developer ggot when she used `rebase` to the `master` branch.

However, following the `master` branch will be trickier. If we rebase our feature branch onto the master branch we
might do so while there are changes in our feature branch on the remote server or at other developers and then this will
totally mess up our history. So don't do that. Instead, have short-lived feature branches.

![](/img/Git-Logo-2Color.png)


<linkto file="examples/git/two-dev-master-merge.sh">

<linkto file="examples/git/two-dev-master-rebase.sh">

<linkto file="examples/git/two-dev-feature-merge.sh">

<linkto file="examples/git/two-dev-feature-rebase.sh">


