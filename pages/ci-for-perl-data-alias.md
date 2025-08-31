---
title: "CI for Data::Alias in Perl - including threaded perl"
timestamp: 2022-12-25T07:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


[CPAN Digger](https://cpan-digger.perlmaven.com/) has a never ending 3rd party Perl libraries, many without any CI configured. This time I picked the one called [Data::Alias](https://metacpan.org/dist/Data-Alias).


At first I sent a "standard" configuration of GitHub Actions, but then I noticed 2 things. Some tests were dependent on some extra modules and some tests needed a threaded Perl. Apparently the one that I used in my "standard" configuration isn't. So In addition to the execution of the CI on Ubuntu, macOS and Windows natively, I've also added another job in which we use a perl-based Docker image and run the tests there. In this case one of the tags I used from [Perl on Docker Hub](https://hub.docker.com/_/perl) was the <b>5.36-threaded</b>.

I was happy to see that the tests passed on every platform and on every version of Perl I tried.

I sent the [pull-request](https://github.com/mvduin/perl-Data-Alias/pull/3)

## GitHub Actions

{% include file="examples/perl/data-alias/ci.yml" %}

## Conclusion

Sometimes you need more than one job even for stand-alone 3rd-party libraries.

