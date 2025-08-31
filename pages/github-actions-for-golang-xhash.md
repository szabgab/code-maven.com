---
title: "Add GitHub actions to the xhash project written in Go"
timestamp: 2022-10-11T15:00:01
tags:
  - GitHub
  - Go
published: true
books:
  - testing
  - golang
author: szabgab
archive: true
show_related: true
---


I went to the [golang](https://github.com/topics/golang?o=desc&s=updated) topic of GitHub sorted by "Recently updated" and looked
at repositories that do not yet have a lot of stars. Most likely they are at an early stage so it might be easier to contribute simple things,
such as tests and GitHub Action configurations.

I found [xhash](https://github.com/ricardobranco777/xhash) package.


As this is the first time I am adding GitHub Actions to a project written in Go I got a bit luck as this one had a Dockerfile
and a Makefile. Thus it was quite obvious how to run the tests.

```
make
make test
```

I also looked at a more popular Golang project to see what they have and based on that I got the following config file
that I saved as <b>.github/workflows/ci.yml</b>. Besides a small typo I got it right and now the CI runs and tests the
code on 6 different platforms.

{% include file="examples/xhash-ci.yml" %}

