---
title: "Testing 3rd party packages on end-user's machine during installation"
timestamp: 2021-06-26T07:30:01
tags:
  - packages
published: true
author: szabgab
archive: true
show_related: true
---


Regardless of the programming language you will probably rely a lot on [3rd party packages (aka. libraries)](/package-registry).
Many packages have automated tests and many package developers run some sort of Continuous Integration (CI) system to verify that
their code works.

They can use a testing matrix to run the tests on a number of different platforms, architectures, and versions of your programming language,
but that's still very far from covering all the possibilities.

In addition they usually test their code with the latest version of their dependencies.

You have good chance that the code was never tested on a system like yours.

How can you be confident that the code you just installed works as expected on your computer as well?


## Test the 3rd party packages on your system!

In the Perl world there are a number of clients for [CPAN](https://www.cpan.org/), the package management
system. The common feature is that by default they run all the automated tests of every dependency as they are
installed recursively. Not only that, but if enabled they can also send the results to a central database
called [CPAN Testers](http://www.cpantesters.org/) where both the author and other users can see the results
and can inspect the failures if necessary.

This system was invaluable before the introduction of the various cloud-based CI services, but even today it provieds a lot of value.
It's data is integrated into [Meta CPAN](https://metacpan.org/), the site where people locate 3rd party Perl packages.
One can easily see the ratio of success and failure reports.

If the current version of the package does not work on your system you can easily locate a version of the package that had passing reports
and you can switch to that version while waiting for a bug-fix to arrive.

I think this is an awesome feature of the Perl ecosystem that I wish other languages have also adopted.

## Speed

The main drawback of the system is running the tests for all the dependencies can take a lot of time.
I mean 10s of minutes. The <b>cpan</b> clients allow you to opt-out and install the dependencies without running the tests.

## Failures

Another issue with this system is the question what happens if a test of a package fails. On one hand it is a good thing as
it probably revealed a situation in which the package does not work properly. If this happens to experienced developers they
will probably know how to report the bug. If this happens to someone who is less experienced or who is new to the language
this might freak them out.

A special case of this is when the failure is due to something incorrect in the tests themselves.

## Design / Wish-list

I think if I could design this myself I would probably make the default not to test. So beginners have a smoother experience.
I would also make it easy to configure the tool to run the tests during the installation.

I would make it possible that the client run the tests selectively only on some of the packages.
For example only the tests of the immediate dependencies, or only the tests of the package the user deem to be very important.

I would also make it easy to run the tests on the already installed packages.

I would definitely have a central database of the reports and let people opt-in to send the reports there.

