---
title: "Jenkins Pipeline: Add some text to the job using manager.addShortText"
timestamp: 2018-08-21T22:30:01
tags:
  - manager
  - addShortText
published: true
books:
  - jenkins
author: szabgab
archive: true
---


This will add text to the specific job on the summary page of the classic UI.
The text does not show up on the BlueOcean UI.


```groovy
script {
   manager.addShortText("Some text")
   manager.addShortText("\ntext")

   manager.addShortText("same line", "black", "lightgreen", "0px", "white")
   manager.addShortText(text, foreground_color, background_color, border_width, border_color)
}
```

For the manager object to exists we need to install the [Groovy Postbuild Plugin](https://wiki.jenkins.io/display/JENKINS/Groovy+Postbuild+Plugin)

{% include file="examples/jenkins/manager_addShortText.Jenkinsfile" %}
