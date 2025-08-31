---
title: "Jenkins report the name of the stage that failed"
timestamp: 2019-05-01T20:30:01
tags:
  - Jenkins
  - STAGE_NAME
published: true
books:
  - jenkins
author: szabgab
archive: true
---


Store the STAGE_NAME in a variable and read it in the post-section

{% include file="examples/jenkins/report_stage.jenkinsfile" %}

