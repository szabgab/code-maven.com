---
title: "Jenkins Pipeline parameters"
timestamp: 2020-12-07T07:30:01
tags:
  - Jenkins
  - parameters
published: true
books:
  - jenkins
author: szabgab
archive: true
show_related: true
---


Jenkins pipelines can declare what kind of parameters it accepts and what are the defaults to those parameters.

Scheduled jobs will use the default values. Users running the job manually can set the parameters.



{% include file="examples/jenkins/parameters.Jenkinsfile" %}

Trying to <b>echo params.secret</b> caused an exception

```
java.lang.ClassCastException: org.jenkinsci.plugins.workflow.steps.EchoStep.message expects class java.lang.String but received class hudson.util.Secret
```

Similarly <b>echo params.yesno</b>

raised this exception:

```
java.lang.ClassCastException: org.jenkinsci.plugins.workflow.steps.EchoStep.message expects class java.lang.String but received class java.lang.Boolean
```

Putting them in string solved the problem for both of them.

I also included a small <b>script</b> that uses the Linux shell to echo the value.

Primarily shoing that even though the content of a <b>password</b> field will not be visible on the UI of Jenkins,
the console log might contain it if we are not careful. Better not to print it.

See [documentation](https://www.jenkins.io/doc/book/pipeline/syntax/#parameters)

