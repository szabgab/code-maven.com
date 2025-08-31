---
title: "How to set the job number and description for a Jenkinsfile in a Jenkins Pipeline?"
timestamp: 2019-12-07T09:35:01
tags:
  - Jenkins
  - currentBuild
  - displayName
  - description
published: true
books:
  - jenkins
author: szabgab
archive: true
---


```
currentBuild.displayName = "hello"  // replaces the job number
currentBuild.description = "world"  // Writes text under the job number
```

