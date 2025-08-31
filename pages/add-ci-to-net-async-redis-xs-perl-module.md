---
title: "Add GitHub Action CI to the Net-Async-Redis-XS Perl module"
timestamp: 2022-12-02T11:30:01
tags:
  - GitHub
  - CI
  - Perl
  - Redis
description: "The preparation was hard, but once I have everything prepared configuring GitHub Actions was quite easy."
types:
  - screencast
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


For the second day of the [2022 December CI Challenge](https://code-maven.com/2022-december-ci-challenge)
I wanted to have a Perl module. Partially because I have working on adding CI to Perl modules for a while.

I looked at [CPAN Digger](https://cpan-digger.perlmaven.com/) where some Perl script collects and analyses
the most recent uploads to CPAN, the central web site of of the Perl packages and [MetaCPAN](https://metacpan.org/)
is the user-friendly place to view the content of all the packages.


When I looked at CPAN::Digger the first package that had a link to its GitHub repository but did not have CI
was the [Net-Async-Redis-XS](https://metacpan.org/dist/Net-Async-Redis-XS) distribution.

I thought that could be a nice challenge as it will probably require having Redis installed on the CI server.

## Background work

Before I could start working on this project I wanted to create an example GitHub Action configuration where
we have a Redis server and it is being access by <b>curl</b>. I wasted a lot of time on this and thought I should
try to do something simpler that I can experiment with on my own computer and I don't need to send it to GitHub
and wait for it do run my code.

So I started to work on a Docker Compose configuration where I had two containers. One is a Redis service and the
other one is a simple client. Here to I failed to use <b>curl</b> as the client.
However, I could make it work using the official Redis client called <b>redis-cli</b>.
I added the example to my [Docker slides](https://code-maven.com/slides/docker/docker-compose-redis-server-and-client).

Once I managed to create the Docker Compose configuration, creating the one running on GitHub Actions was easier. You can find
my example in [this repository](https://github.com/szabgab/github-actions-redis/).

I 08 2-3 hours on the preparations, but I also created the examples so people will be able to base their work on these examples.

## Creating the GitHub Action using Redis

Once I had the Redis configuration the work on the Perl module was not that hard.
I made a few typos and missed the fact that the repository has a <b>Makefile.PL</b> so at first I tried to use <b>Dist::Zilla</b>.

I also had to include the installation of a few Perl modules in the GitHub Action configuration. I am not sure why is that.
Are they really missing from the list of dependencies of the module? If yes, how does it even get installed by users?
Did I miss a step that would have installed them?

I'll leave the discussion about this for later, after the initial version of the CI is enabled.

## Supported versions of Redis and Perl

I added 3 versions of Redis to the matrix and tried a number of versions of Perl, but it worked only with Perl 5.36.

Also I only tried this inside a Linux-based Docker container. Not on Windows and not on Mac OSX. I don't know if the module
is even intended to support those platforms.

## Adding a test

After sending the Pull-reques I went for a long walk. That helped me realize that I never told the tests what is the hostname of the
Redis servers. So I guess the tests of the module never actually tried to access the server.

When I got back in-front of the computer I looked at the tests and indeed they were very shallow never trying to execute any
operation that would need a server. So I created one, basically copying the example in the documentation of the module and put it in the
<b>t</b> directory where it belongs. The test will received the name of the Redis host via an environment variable called <b>REDIS_HOST</b>.
If this variable is not set these tests will be skipped. You can see the test-file here:

{% include file="examples/Net-Async-Redis-XS/set_get.t" %}

I've also update the GitHub Action configuration file so it will set the <b>REDIS_HOST</b> environment variable to <b>redis</b>,
the name of <b>redis service</b> that was included in the configuration file.


## GitHub Actions configuration file

I've included here the configuration file for future reference as the one in the project, if it even gets accepted, will probably change.

{% include file="examples/Net-Async-Redis-XS/ci.yml" %}

## Pull-Request

I sent the [Pull-Request](https://github.com/team-at-cpan/Net-Async-Redis-XS/pull/1). Let's see if it gets commented on or accepted.

