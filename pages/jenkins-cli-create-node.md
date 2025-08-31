---
title: "Jenkins CLI: create node"
timestamp: 2018-08-22T08:30:01
tags:
  - jenkins-cli
published: true
books:
  - jenkins
author: szabgab
archive: true
---


In some situation you might need to add nodes (aka. agents) programmatically to a Jenkins setup.
This is a shell script to register the new node based on the [gist of Christopher Davenport](https://gist.github.com/ChristopherDavenport/bc5ba7a33d5dd5fc975da81c4a270a90).


{% include file="examples/jenkins/create-jenkins-node.sh" %}


Notes:

* "Agent" and "node" is often used interchangably and in the old days they were called "slaves" so you will still see that word used in some documentation and in the code.
* The origrinal name of the Jenkins project was Hudson and that too still appears in a lot of the code.
* remove the -remoting flag
