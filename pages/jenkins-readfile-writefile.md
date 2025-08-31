---
title: "Jenkins Pipeline: read a file and write a file - readFile, writeFile"
timestamp: 2020-01-06T20:30:01
tags:
  - readFile
  - writeFile
published: true
books:
  - jenkins
author: szabgab
archive: true
---


In the following Jenkinsfile we have two stages. In the first stage we create a variable called <b>data</b> that
holds some text and the we use the <b>writeFile</b> function to write it out to a file.
Then we execute <b>ls</b> as an <a href="/jenkins-pipeline-running-external-programs">external program using <b>sh</b></a>.

In the second stage we use the <b>readFile</b> function to read in the content of the file.


{% include file="examples/jenkins/readfile-writefile.txt" %}

