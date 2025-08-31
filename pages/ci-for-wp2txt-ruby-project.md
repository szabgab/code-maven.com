---
title: "CI for wp2txt Ruby project"
timestamp: 2022-12-11T08:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


After the success yesterday [adding CI to a Ruby Gem](https://code-maven.com/ci-for-rdf-kv-ruby) I thought I can give another
try to more Ruby Gems so I looked at the [Ruby Digger](https://ruby-digger.code-maven.com/). As I can see there is even less action
there than on [CPAN Digger for Perl](https://cpan-digger.perlmaven.com/).


## Error reports

First I looked at a project called [nezekan](https://github.com/zarkiel/nezekan). I tried to run the tests locally, but failed.
I am not sure if I was even trying to run them as the authors intended, but [this error](https://github.com/zarkiel/nezekan/issues/1) seem
to be genuine. It is a case-sensitivity issue. After I fixed that locally I bumped into [and reported another issue](https://github.com/zarkiel/nezekan/issues/2).

Only now, that I am writing this I realized that the project had a Travis-CI configuration file. Although Travis-CI does not provide the free service any more
I could have looked at the configuration file and base my commands on that. I can get back to that later.


## wp2txt

After a while I found the [wp2txt](https://github.com/yohasebe/wp2txt) project. Adding GitHub Actions to this was quite simple
though it was different from the previous one. Here is the [pull-request](https://github.com/yohasebe/wp2txt/pull/11)
and below you'll find a copy of the configuration file as I sent it.

## GitHub Actions

{% include file="examples/wp2txt/ci.yml" %}

## Conclusion

Slowly, but I learn how to run the tests in the various Ruby projects as well. Unfortunately there are not very many new uploads to [RubyGems](https://rubygems.org/)
and this [Ruby Digger](https://ruby-digger.code-maven.com/) is growing slowly.


