---
title: "Jenkins pipeline: List agents by name or by label"
timestamp: 2020-07-03T18:00:01
tags:
  - Jenkins
  - instance
  - computers
  - getLabels
  - displayName
published: true
books:
  - jenkins
author: szabgab
archive: true
show_related: true
---


## List agents by name and by label

```
def jenkins = Jenkins.instance
def computers = jenkins.computers
computers.each {
   //  println "${it.displayName} ${it.hostName}"
}

def labels = jenkins.getLabels()
labels.each {
   println "${it.displayName}"
}
```


