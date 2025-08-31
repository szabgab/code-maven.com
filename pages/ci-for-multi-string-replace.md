---
title: "CI for multi_string_replace Ruby Gem"
timestamp: 2022-12-21T06:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


[multi_string_replace](https://rubygems.org/gems/multi_string_replace) was one of the projects I started a yesterday and could not finish as there was an issue. I reported the issue and within a few hours the author pointed at a command I needed to include to make it work. Here is what happened:


I cloned the git repository and launched an Ubuntu 22.10-based Docker container I use to try these packages. Followed the instructions in the README file: Executed <b>./bin/setup</b> and then ran <b>rake spec</b>. I got a nasty error message. As I saw already too many other Gems not working properly I did not investigate this one. Just reported it: [rake spec failed: LoadError: cannot load such file -- multi_string_replace/multi_string_replace](https://github.com/jedld/multi_string_replace/issues/5).

As I was looking at the README I also noticed that it has two links that are supposed to point to the GitHub repository, but there was a placeholder <b>[USERNAME]</b> instead of the actual username. I fixed that and sent a [pull-request](https://github.com/jedld/multi_string_replace/pull/6).

Soon the author accepted and integrated the PR and replied that I was missing the <b>rake compile</b> step.

Fair enough, but it was missing from the README as well. Probably because this README was a generated file and for pure-ruby Gems you don't need this extra step.

I tried it in my Docker container and it worked. I tried in GitHub Actions and it worked there too.

So I sent a [pull-request](https://github.com/jedld/multi_string_replace/pull/7) adding this instruction to the README  and then sent a [pull-request](https://github.com/jedld/multi_string_replace/pull/8) adding GitHub Actions.

Both were accepted and integrated very quickly. I like this. Such quick action encourages contributors because their work starts to be useful very quickly. (even if that "work" is only fixing something in the README.)

## GitHub Actions

The GitHub Actions configuration file can be seen here:

{% include file="examples/python/multi_string_replace/ci.yml" %}

## Conclusion

It is always a good idea to report the issues you encounter with software. Sometimes the author will react within a few hours and then you can make progress with whatever you were planning to do.


