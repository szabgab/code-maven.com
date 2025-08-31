---
title: "Moving from Travis-CI to GitHub Actions for Marpa::R2"
timestamp: 2022-12-16T07:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


[Marpa::R2](https://metacpan.org/pod/Marpa::R2) can parse any language whose grammar can be written in BNF.
It used Travis-CI, but since Travis-CI discontinued its free offering for Open Source project the project was without CI.

I [asked](https://github.com/jeffreykegler/Marpa--R2/issues/289) the author if he would be interested in a GitHub Actions
configuration.


## A warning during build

I tried to build the module locally and run its tests locally, but I encountered some issues:

First I noticed that there are some [warning during the build](https://github.com/jeffreykegler/Marpa--R2/issues/290)
emitted by one of the dependencies. As it turns out upgrading the dependency solved this issue, but the latest package
of the dependency also had a minor issue. The version numbers in the different files were slightly confusing.
So I [reported that too](https://github.com/Perl/perl5/issues/20609).

Apparently that was already fixed, it was just not released yet.

## An error - missing files

The next thing I encountered was that some files were [missing](https://github.com/jeffreykegler/Marpa--R2/issues/291).
That made the tests fail. The author first thought that the issue was somehow cause by me mixing versions, but soon found that the
files were <b>not added to git</b>.

This is one of the reasons to have CI.

This can happen to any one of us.

Maybe not to you, but someone else on your team or to a contributor to your project

## Should the tip of the main branch be usable?

The author made an interesting [comment](https://github.com/jeffreykegler/Marpa--R2/issues/291#issuecomment-1353354424) on the  [issue](https://github.com/jeffreykegler/Marpa--R2/issues/291) about the missing files.

<quote>
FYI many programmers make a point of the tip of their main branch being something usable. I am NOT one of them, so pulling from my repo, instead of a distribution, is risky.
</quote>

Here is what I think about it:

I would say it is a good practice to ensure all the test are always passing on the tip of the main branch.  Otherwise one would risk starting to think that "some tests always fail" which could lead to some test failing that *should not fail* go unnoticed for a long period of time.

Also it upsets the CI and we don't want to do that.

Actually, one of the reasons of having a CI to have something look over our shoulders and make sure that all the tests are always passing on a clean environment.

And then comes the point, if all the tests are passing, doesn't that mean that the version is usable?

I am looking forward the continuation of this discussion.

## Pull-Request

Once those issues were fixed adding the GitHub Action configuration file and converting the commands from the Travis-CI config file to GitHub Actions
was not difficult. At one point the author commented that he wants the code to run on Windows and macOS as well, but it is difficult as he does not have
access to those operating systems. I figured configuring GitHub Actions to run on those OS-es as well will help him with that task. I was also expecting
the test or even maybe the compilation to fail on at lest one of them. So I was a bit surprised that everything worked.

Well, I still managed to make a few mistakes and thus had to try it several time, but after a while I got it right and sent the [pull-request](https://github.com/jeffreykegler/Marpa--R2/issues/291).
To my surprise the author closed it as he is planning to move the repo to a GitHub organization.

It is unclear to me why that stops him from accepting the PR so I asked him on the PR.

## GitHub Actions

In any case, I included the configuration files here. This time, I went a bit further than in the previous cases of my recent GitHub Actions pull-requests.
I also went beyond what was in the Travis-CI configuration file.

This time I create two configuration file.

In the first one we use multiple version of perl in Docker containers.

{% include file="examples/marpa-r2/ci.yml" %}

In the second one we use the 3 different operating systems: Windows, Linux and macOS.

{% include file="examples/marpa-r2/native.yml" %}

## Conclusion

You don't have to have a CI if you remember always running your tests. You don't even need to have access to Windows and macOS to make your code work there if you are a really good
programmer as Jeffrey Kegler, the author of Marpa. And even then you might forget to add some of the files to git.

However, most of us aren't as focused on the details and most of would not be able to build a project like Marpa. For sure I know I wouldn't.

So we need the hand-holding and the discipline a CI can provide.

