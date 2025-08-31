---
title: "Jenkins Pipeline printing Unicode characters"
timestamp: 2020-10-03T18:30:01
tags:
  - Jenkins
description: "It seems to be easy to print Unicode characters from a Jenkins Pipeline"
published: true
books:
  - jenkins
author: szabgab
archive: true
show_related: true
---


It seems to be easy to print Unicode characters from a Jenkins Pipeline


{% include file="examples/jenkins/unicode.jenkinsfile" %}

I tried this in Jenkins version 2.249.1 running in Docker and the consul output was showing the strings as expected.
