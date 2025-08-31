---
title: "CI for the draftjs_html Ruby Gem"
timestamp: 2022-12-20T07:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


It took me quite a few failed attempts on various Ruby Gems found on the [Ruby Digger](https://ruby-digger.code-maven.com/) till I found one that passed its tests. I reported the failures for the others, but this is getting a bit frustrating.


## Default setup

I noticed that many Ruby Gems have the same instructions to set up the development environment and to run the tests. I guess this means they used some tool to generate the skeleton of the project that automatically created the `bin/setup` shell script and the test spec files that  could be filled.

One one hand this is good as it probably encourages people to start writing test-specs.

On the other hand having a bash script to execute `bundle install` means we cannot use this on Windows natively. So for Windows we need different instructions. I think this isn't such a good idea.

## Travis-CI

It seems that the script creating the Ruby Gem skeleton also include a configuration file for Travis-CI. Unfortunately Travis-CI does not work any more for free so this file just sits there and has no purpose. It even causes confusion because it gives the feeling that the the tests worked at least once in Travis, even for Ruby projects that were created after Travis-CI stopped its public service.

## GitHub Actions

Anyway, for this particular Ruby Gem the instructions worked so I could configure GitHub Actions and send a [pull-request](https://github.com/dugancathal/draftjs_html/pull/4)

{% include file="examples/draftjs-html/ci.yml" %}

## Conclusion

There are many projects that don't have working CI (maybe have a Travis-CI configuration, but that does not do anything now), and their tests fail. I am actually a bit surprised about this even though this is one of the reasons I think it is important to have a functioning CI set up, so that you will be reminded if you forget to run the tests and they break.


