---
title: "GitHub Workflow for ruby-request-builder"
timestamp: 2022-12-18T06:30:01
tags:
  - GitHub
published: true
books:
  - github
author: szabgab
archive: true
show_related: true
---


Today, while looking at the newly fixed [Ruby Digger](https://ruby-digger.code-maven.com/) I noticed a gem called [request-builder](https://rubygems.org/gems/request-builder). It had Travis-CI configured. However, Travis-CI stopped its free service a while ago. I thought I check this out.


## Instructions

This project has instruction in its README file how to set it up locally and how to run its tests. This is awesome as it seems there are several ways to do this depending on the preferences of the author.

## Error in tests

I cloned the repo, started my Docker container where I run the tests, installed the dependencies and then got an error while running the tests. I [reported](https://github.com/RainbowPonny/ruby-request-builder/issues/1) it.


## Find the breaking change

Then I thought, if the author used Travis-CI then this surely worked at one point. So I looked at the history.

In my `~/.gitconfig` I have an alias:

```
[alias]
  lg = log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit
```

So I just ran

```
git lg
```

And got this output:

```
* 8a160e5 - (HEAD -> main, origin/main, origin/HEAD) Bump version to 0.2.1 (7 hours ago) <Anton Kostyuk>
* 1ef292c - Add config dup method (7 hours ago) <Anton Kostyuk>
* 7a079f2 - Bump version (8 hours ago) <Anton Kostyuk>
* e21a35d - Bump version (8 hours ago) <Anton Kostyuk>
* a954ffd - Fix headers, params, callbacks inheritance (8 hours ago) <Anton Kostyuk>
* 6b1cdf7 - Fix config duplication (3 weeks ago) <Anton Kostyuk>
* 21381bf - Bump version (3 months ago) <Anton Kostyuk>
* c59c152 - Add default adapter method (3 months ago) <Anton Kostyuk>
* 97e6f11 - Fix initializing (3 months ago) <Anton Kostyuk>
* c7fc920 - Update README.md (3 months ago) <Anton Kostyuk>
* 4bf2717 - Bump version to 0.1.1 (3 months ago) <Anton Kostyuk>
* 4b06d19 - Update description and links (3 months ago) <Anton Kostyuk>
* c61eb20 - Update README.md (3 months ago) <Anton Kostyuk>
* 4ecb8e5 - Add tests (3 months ago) <Anton Kostyuk>
* 617a0c8 - Fix gem initialize (3 months ago) <Anton Kostyuk>
* ce87ffd - Fix files load (3 months ago) <Anton Kostyuk>
* 0cb0466 - Init (3 months ago) <Anton Kostyuk>
```

I noticed that there were a few changes 7-8 hours again. A change 3 weeks ago and the original code was written 3 months ago. So I said, I said let's try the commit from 3 weeks ago.

I checked it out, ran the tests and they all passed. So I checked out the next commit and the tests already failed. I did not even have to run `git bisect` and found and reported the problematic commit. I hope it will help the author fix the code and/or the tests.

## GitHub Workflow file

The configuration file was straight forward. Almost exactly as we had yesterday. I copied it from there. The only difference is that now we run

```
./bin/setup
rake spec
```

in the docker containers but we run

```
bundler install
rake spec
```

when we run natively. Especially because Windows would not know what to do with the `/bin/setup` shell script.

## Conclusion

The projects with the Travis-CI configuration might be even more in danger than those without any CI configured. They might be in the false security that they have a CI while it has not been working for quite some time.

It's a real pity that Travis-CI shut down their free service. I liked them. I don't know what has happened though I guess as GitHub Actions took over their business they could not afford it any more.
