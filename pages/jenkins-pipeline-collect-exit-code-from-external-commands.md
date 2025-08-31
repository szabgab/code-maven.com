---
title: "Jenkins Pipeline: Collect exit code from external commands"
timestamp: 2020-07-03T13:30:01
tags:
  - Jenkins
  - bat
  - returnStatus
published: true
books:
  - jenkins
author: szabgab
archive: true
show_related: true
---


Instead of killing the whole job on a single failure we can capture the exit code of external programs,
collect them and report at the end if one of them failed.


## Collect exit code of commands

```
def commands = ["xyz", "abc", "pwd"]
def errors = ''
commands.each {
    def res = sh(script: it, returnStatus: true)
    println("cmd: $it res $res")
    if (res !=0 ) {
        errors += " $it"
    }
}
//if (params.expected == 'Success') {
//    sh "pwd"
//} else {
//    sh "xyz"
//}
if (errors) {
    error(errors)
}

```

{JENKINS+_URL}/pipeline-syntax/globals

{% include file="examples/jenkins/experiment.jenkinsfile" %}
