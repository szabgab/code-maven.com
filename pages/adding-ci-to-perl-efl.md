---
title: "Adding CI to Perl::Efl - sometimes you need to do some extra work"
timestamp: 2022-12-08T09:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


[Originally](https://code-maven.com/2022-december-ci-challenge) I wanted to do a very diverse set of CI configurations during December,
but so far I was only successful on Python and Perl packages. I failed on a number of Ruby packages and I have not even really search anything else.
This is partially due to the fact that I am a lot more familiar with the first two languages than with anything else and I don't have enough time
for the others. At least not while I "have to" send the PR every day.

Today I picked another Perl module. As it turned out it wasn't such a "low-hanging-fruit" either as I was hoping for, but I managed to set up CI.
At least on Ubuntu.


[pEFL](https://metacpan.org/release/pEFL) is the name of the Perl bindings for the [Enlightenment Foundation Libraries](https://www.enlightenment.org/).

According to the README of the Perl Module one needs to install the <b>efl-dev</b> package, but on Ubuntu 22.10 there is no such package. I found one called
<b>efl-doc</b>, but that's the documentation. Running <b>apt-cache search efl | grep dev</b> helped me find the package called <b>libefl-all-dev</b>.
It seem that this is what we needed. So I opened an [issue](https://github.com/MaxPerl/Perl-Efl/issues/2).

At first I was trying to run the tests directly on the <b>ubuntu-latest</b> runner of GitHub Actions, but soon I gave up.
Maybe the problem was that it is running an older version of Ubuntu. Maybe the problem was something else. I don't know, I have not researched it.
Instead I switched to using the official Ubuntu 22.10 docker image.

After several trial and error I figured out that I have to also install the <b>gcc</b> and <b>make</b> packages for the compilation.

For Perl I needed [ExtUtils::PkgConfig](https://metacpan.org/pod/ExtUtils::PkgConfig).
The easiest seemed to be to install the <b>libextutils-pkgconfig-perl</b> package that is packaged and distributed by the developers of Ubuntu.

At the end I saw that the only test this package has is trying to load the module, but at least we can see that the compilation worked.

## CentOS

After the success with Ubuntu I thought I'll also try to do the same on a CentOS based Docker container. I started with CentOS 7.
I found out it does not even have Perl installed so I started with that. However, when I got to the installation of the <b>efl</b>
library I found out that it is not available on CentOS. At least not in the default locations.

At this point I decided to stop for now and sent the [Pull-Request](https://github.com/MaxPerl/Perl-Efl/pull/1) with the Ubuntu configuration.
Better to have one than none. Later we can try to figure out how to set this up on other Linux distributions. Maybe with different versions of Perl as well.

If the author even interested.

## Why is this valuable?

While I was still composing this blog post, the author has updated the README file, closed the issue and commented on it indicating that
it is unclear what is the purpose of compiling / running tests on every push?
Unfortunately not all distributions have efl/Enlightenment. But compiling the libraries is not a hard job...
Perhaps the <a href="https://blog.buddiesofbudgie.org/"Budgie Desktop</a> switch to efl, then the distribution coverage could be better...

Let me answer it here as I think this could be interesting to others as well.

The point of CI running on every push is to get feedback as soon as possible.

It would be a lot more valuable if there were lots of tests than just loading the module as in this case,
but even this way it is valuable to see if some change broke some part of the code that the developers have not noticed on their computer.

If the changes came as Pull-Request then the author does not even know if the sender has tried to compile the code on their computer. Maybe they just sent some changes?
By letting the CI compile it both the author and the PR sender will quickly see the results. That can save time to the author and the PR sender might even fix the issue
before the author has a chance to look at it.

It would be more useful if the compilation was done on various Linux and BSD distributions and maybe using various versions of Perl.
If the specific distribution does not have a ready-made package of Efl then it could be possibly compiled from its source code.
It is very unlikely that the author has many setups locally and it is even less likely that a potential contributor has all that setup.
Even if they have it is probably easier to hand this job off to some external system (GitHub Actions in this case) than doing on your computer.
So on the longer run it will be a lot more beneficial to set this up on other distributions as well.
Consider this PR as the first step in that direction.

I have a [video talking about this](https://code-maven.com/travis-ci-why-use-continuous-integration), though in that I was talking about Travis-CI.

## GitHub Actions for Ubuntu

{% include file="examples/perl-efl/ubuntu.yml" %}

## Partial configuration for CentOS

{% include file="examples/perl-efl/centos.yml" %}

## Conclusion

Better one bird in the hand than two birds on the tree. Or some similar expression.


