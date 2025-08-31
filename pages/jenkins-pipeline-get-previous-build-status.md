---
title: "Jenkins pipeline: Get previous build status - getPreviousBuild"
timestamp: 2020-07-03T17:00:01
tags:
  - Jenkins
  - currentBuild
  - getPreviousBuild
published: true
books:
  - jenkins
author: szabgab
archive: true
show_related: true
---


## Jenkins get previous build status

```
println(currentBuild.getPreviousBuild())
println(currentBuild.getPreviousBuild().result)
```



