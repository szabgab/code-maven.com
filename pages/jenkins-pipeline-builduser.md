---
title: "Jenkins Pipeline BuildUser plugin"
timestamp: 2019-02-15T13:30:01
tags:
  - Jenkins
  - BuildUser
  - BUILD_USER_EMAIL
  - BUILD_USER_ID
  - BUILD_USER
  - BUILD_USER_FIRST_NAME
  - BUILD_USER_LAST_NAME
published: true
books:
  - jenkins
  - groovy
author: szabgab
archive: true
---


[Build User Vars Plugin](https://wiki.jenkins.io/display/JENKINS/Build+User+Vars+Plugin)
also known as [build user vars plugin](https://plugins.jenkins.io/build-user-vars-plugin)



Install:

On the Jenkins UI click on Jenkins - Manage Jenkis - [Manage Plugins](http://localhost:8080/pluginManager/) - Available
filter for <b>user build vars</b>, check the checkbox and click on "install without restart".

This is a sample Jenkinsfile showing how to use it.

{% include file="examples/jenkins/builduser.Jenkinsfile" %}

In order to make the variables available you need to have your code wrapped in:

```
wrap([$class: 'BuildUser']) {
}
```

Sometime it is inconvenient to do that for the whole code, so inside the wrapper, you can copy the values to
Other variables that can be then accessed outside of the wrapper as well.


See also [Jenkins pipeline: get current user](/jenkins-get-current-user) using currentBuild and getBuildCauses.
