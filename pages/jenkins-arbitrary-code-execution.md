---
title: "Jenkins pipelines: Arbitrary code execution in the shell"
timestamp: 2020-01-16T08:40:01
tags:
  - sh
  - parameters
  - currentBuild
  - getBuildCauses
published: true
books:
  - jenkins
author: szabgab
archive: true
---


It is quite common that what works on the developers computer does not work on the Jenkins Agent. Experimenting by committing code-changes to the Git repository
and letting the Jenkins job pick it up can be time consuming and quite annoying having all those commits in the history.

One, admittedly strange solution is to let your user execute any command on the Jenkins server without giving them ssh access.


This code snippet can be used as a Jenkins Pipeline. It has a single parameter where you can type in anything.
The job will execute it as a shell command.

Be warned though, this allows <b>any</b> code executed by anyone who can run that job on the Jenkins server.

{% include file="examples/jenkins/shell.Jenkins" %}


A slightly better way to do this is to include a list of users who can run the code and check the username
before running the shell command:

{% include file="examples/jenkins/shell_with_authorization.Jenkins" %}

We use the [get current user](/jenkins-get-current-user) (currentBuild, getBuildCauses) to have some
authorization. We could have also used the [BuildUser plugin](/jenkins-pipeline-builduser).
