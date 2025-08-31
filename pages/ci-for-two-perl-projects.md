---
title: "CI for Mojo-UserAgent-Cached and Plack-Middleware-Greylist"
timestamp: 2022-12-09T17:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


Today I can report about two pull-requests for two web-related Perl projects.
One of them is called [Mojo-UserAgent-Cached](https://metacpan.org/dist/Mojo-UserAgent-Cached)
and the other one is [Plack-Middleware-Greylist](https://metacpan.org/dist/Plack-Middleware-Greylist).


## Mojo-UserAgent-Cached

It was quite straight-forward. There were only two small issues.
I had to install [Module::Install](https://metacpan.org/pod/Module::Install) before I could use the regular tools
as the <b>Makefile.PL</b> relies on that. That's a known drawback of Module::Install for developers and maintainers.

The other problem was that tests were failing on Windows so I had to disable them.
Anyway I sent a [Pull-request](https://github.com/nicomen/mojo-useragent-cached/pull/6) it was merged soon after.

{% include file="examples/mojo-useragent-cached/ci.yml" %}

## Plack-Middleware-Greylist

Here too I had to disable the testing on Windows, this time because one of the dependencies was failing own Windows.
The author then wanted to add testing more versions of Perl, but did it himself. I was contemplating a bit if I should send
another PR where first we build the tar.gz on one version of Perl and then use that for testing, but there are no
extra dependencies install for the building so I don't think that could reduce the time or the cpu usage.

[pull-request](https://github.com/robrwo/Plack-Middleware-Greylist/pull/3)

{% include file="examples/plack-middleware-greylist/ci.yml" %}

## Conclusion

That was easy.

