---
title: "Why to have Public Version Control System for Open Source Projects?"
timestamp: 2017-08-27T14:30:01
tags:
  - Git
  - Subversion
  - VCS
  - Perl
  - Python
published: true
author: szabgab
archive: true
---


It is still not a universally accepted best practice, but these days most of the
companies already use some kind of a version control system for their software development.

Some people still find the version control systems a burden, but with further education
I think this can be improved.

In my experience open source projects had a much better track record using version control systems,
but there are still many individuals who write open source code without a public version control system.

Some might not even use a version control system, though I think that's quite rare.


One of the key features of Open Source is that other people can change the code and <b>contribute to the project</b>.

## What if there is no public VCS?

If there is no public version control system (VCS) the users who would like to improve the code will need to base their changes
on the most recently published version of the code.

This might mean that the bug they are trying to fix has already been fixed, but it has not been released. That would be both a <b>waste of time and a waste of goodwill</b>.

Two or more people might be solving the same issue during this period without knowing about each others effort. Again, more <b>waste of energy</b>.

If there is no public VCS, the potential contributor will have to create a `diff`, send it by e-mail and the author also needs
to manually handle the process using `patch`. This is how it was done before, but we can do much better today.

<b>Lack of history</b>: Without a public version control system it will be impossible for potential contributors to see the history of your project.
For example to see where and why a bug might have been introduced.
Even if they have access to several released versions of your code, collecting
and comparing those versions is much harder than looking at the log of a version control system.
Even if they manage to build the history, they can only see changes from released version to
released version which probably contain many unrelated changes.

## Let's be positive

Instead of pointing out the negative aspects of not having a public VCS, let's try to see how a public VCS improves life:

Slightly unrelated, but I have to get this out of my system: having a <b>public bug tracking system</b> makes it much easier for people to report bugs and see what are the already reported bugs.

Having a <b>public VCS coupled with a bug tracker</b> will improve your overall development process and will
probably help improving the quality of your code. (And probably the quality of your programming life.)
What "coupled" might mean in this context is that the tickets in the bug-tracking system
and the commits (check-ins) in the version control system can easily refer to each other.

Having a public VCS like GitHub enables [decoupling of core vs contributor](/why-is-git-better-than-subversion-for-open-source-projects) open source teams.

## Using GitHub

While there are other options for having Public Version Control System, these days Git, and [GitHub](http://github.com/)
seems to be the de-facto standard. Not only does GitHub provide free repository for your open source projects, it also makes it
super easy for potential contributors to send in their patches. GitHub makes it extremely easy for you to merge them if you accept
the changes or discuss them if they need further work.

Having a GitHub account can help you with employment. In the answer to the question
[Why is there an emerging notion that people who don't use Github are bad programmers?](https://www.quora.com/Why-is-there-an-emerging-notion-that-people-who-dont-use-Github-are-bad-programmers)
[Mattias Petter Johansson](https://github.com/mpj) pointed out that having an active GitHub account can help potential employers assess the quality of your code and even
your attitude toward other programmers. So while this has nothing to do with your own projects it can be a valuable asset to you.

## Version control of open source projects

In order to see how widespread is the use (or the lack of use) of public version control systems, I've started to collect
information about the use of public VCS-es in Open source projects.

We can check the [recent Perl modules on CPAN](https://perlmaven.com/recent) to see which one
[has no repository in the META files](http://cpan.perlmaven.com/#lab/no-repository) and which on
[has no "license" field in the META files](http://cpan.perlmaven.com/#lab/no-license).

On the [stats page of PyDigger](http://pydigger.com/stats) you can see that about 66% of the Python packages have a GitHub repository
we could identify. Some of the others still might have GitHub repository or some other public VCS, but the [PyDigger](http://pydigger.com/)
system could also be improved.

Libraries of other languages could be also researched.

If you are interested in contributing to one of the projects that does not have an (obvious) public VCS, the first thing I'd ask the main developer
is a link to the VCS. If they don't have one, you might want to reconsider contributing to that project, or if you have a lot of energy you might volunteer to introduce
version control to the developer.

<img src="/img/Git-Logo-2Color.png" alt="Git logo">

