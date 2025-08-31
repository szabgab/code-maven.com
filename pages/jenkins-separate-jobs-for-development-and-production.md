---
title: "Jenkins: separate jobs for development and production"
timestamp: 2020-01-04T22:30:01
tags:
  - Jenkins
  - currentBuild
  - projectName
published: true
books:
  - jenkins
author: szabgab
archive: true
---


When we would like to improve the code of a Jenkins pipeline (and if we don't use branches)
we might want to set up 2 jobs with two separate Jenkins files. One for production and one for
development.


We would work on the development file and then copy over the change to the production file.
Moving the changes manually is very error-prone. It would be much easier to copy the whole Jenkinsfile.

However, we probably want the job to run slightly differently in development than in production.
For example in production we might send an e-mail to the whole team. In development we might want to
only send it to the current developer or not at all.

But how can the code know if the Jenkinsjob is the development job or the production job?

By its name.

This code helps you let's you decide, based on the name of the Jenkins project if you are running under production or development.

```
if (currentBuild.projectName == 'production-name') {
    println("Production code")
} else {
    println("Development code")
}
```
