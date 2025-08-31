---
title: "Jenkins pipeline: add badges"
timestamp: 2020-07-03T18:40:01
tags:
  - Jenkins
  - manager
  - addBadge
published: true
books:
  - jenkins
author: szabgab
archive: true
show_related: true
---


## Add badges

For the manager object to exists we need to install the [Groovy Postbuild Plugin](https://wiki.jenkins.io/display/JENKINS/Groovy+Postbuild+Plugin)


[badge](https://jenkins.io/doc/pipeline/steps/badge/)


```
   manager.addBadge("error.gif", "Failed build")
   manager.addBadge("star-gold.gif", "Successful build")
```

