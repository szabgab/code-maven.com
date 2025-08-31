---
title: "Jenkins Pipeline - set and use environment variables"
timestamp: 2019-02-15T18:30:01
tags:
  - Jenkins
  - Devops
  - printenv
  - sort
  - sh
  - environment
published: true
author: szabgab
archive: true
---




## How to list the environment variables available to Jenkins Pipeline

{% include file="examples/jenkins/list_environment.Jenkinsfile" %}

In this example we list the environment variables using the <b>printenv</b> command of Unix/Linux
which we pipe through the Unix <b>sort</b> command so we'll see the environment variables in a sorted list.

We invoke it using the <b>sh</b> command of the Jenkins Pipeline.

Before we do that we set a new variable called "color" in the <b>environment</b> section of the Jenkins Pipeline.

On Unix/Linux:

```
sh('printenv | sort')
```

On Windows you could run:

```
bat('set')
```

The output will looks something like this:

```
BUILD_DISPLAY_NAME=#18
BUILD_ID=18
BUILD_NUMBER=18
BUILD_TAG=jenkins-list_environment_variables-18
BUILD_URL=http://localhost:8080/job/list_environment_variables/18/
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/110/bus
EXECUTOR_NUMBER=1
HOME=/var/lib/jenkins
HUDSON_COOKIE=40cd788e-91bd-4ebd-86c9-c10333fa27a9
HUDSON_HOME=/var/lib/jenkins
HUDSON_SERVER_COOKIE=912830efeb6e2316
HUDSON_URL=http://localhost:8080/
JENKINS_HOME=/var/lib/jenkins
JENKINS_NODE_COOKIE=dbf878e6-0ae5-4ffe-a32c-aa7876f975ce
JENKINS_SERVER_COOKIE=durable-f6e3ca8e5d2310d4d5695d128db1ea2f
JENKINS_URL=http://localhost:8080/
JOB_BASE_NAME=list_environment_variables
JOB_DISPLAY_URL=http://localhost:8080/job/list_environment_variables/display/redirect
JOB_NAME=list_environment_variables
JOB_URL=http://localhost:8080/job/list_environment_variables/
LANG=C.UTF-8
LOGNAME=jenkins
MAIL=/var/mail/jenkins
NODE_LABELS=master
NODE_NAME=master
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games:/snap/bin
PWD=/var/lib/jenkins/workspace/list_environment_variables
RUN_CHANGES_DISPLAY_URL=http://localhost:8080/job/list_environment_variables/18/display/redirect?page=changes
RUN_DISPLAY_URL=http://localhost:8080/job/list_environment_variables/18/display/redirect
SHELL=/bin/bash
SHLVL=1
STAGE_NAME=example
USER=jenkins
WORKSPACE=/var/lib/jenkins/workspace/list_environment_variables
XDG_DATA_DIRS=/usr/local/share:/usr/share:/var/lib/snapd/desktop
XDG_RUNTIME_DIR=/run/user/110
XDG_SESSION_ID=c1
_=/usr/bin/daemon
color=blue
```

## List the environment variables without running the shell

The `env` object is of type
[class org.jenkinsci.plugins.workflow.cps.EnvActionImpl](https://javadoc.jenkins.io/plugin/workflow-cps/org/jenkinsci/plugins/workflow/cps/EnvActionImpl.html).

{% include file="examples/jenkins/list_environment_internally.Jenkinsfile" %}

We use the <b>getEnvironment</b> method that returns a [hudson.EnvVars](https://javadoc.jenkins-ci.org/hudson/EnvVars.html) object.
This is a Groovy map so we can already use the <b>each</b> method to go over the keys and values.

This however only seem to list the internal variables of Jenkins and for example <b>PATH</b> was not
in the list even though we can access it as <b>env.PATH</b>.


## How to set environment variables in Jenkins?

As also seen above, a section called `environment` can be added to the pipeline

```
environment {
    SOME_NAME = "some value"
}
```

Then it can be accessed using the following syntax:

```
env.SOME_NAME
```



```
pipeline {
   agent none
   environment {
       field = 'some'
   }
   stages {
       stage ('Preparation') {
           agent { label 'master'}
           environment {
               JENKINS_PATH = sh(script: 'pwd', , returnStdout: true).trim()
           }
           steps {
               echo "Hello world"
               echo "PATH=${JENKINS_PATH}"
               sh 'echo "JP=$JENKINS_PATH"'
          }
      }
   }
}
```


## How to use environment variables in the environment section of Jenkins?

```
environment {
    PATH = "/path/to/dir:${env.PATH}"
    JNK_PATH = "${env.WORKSPACE}\\subdir"
}
```

The above only works when the environment section is inside a "stage" but would yield "null" for
WORKSPACE outside the stages.

## Set environment executing code

```
environment {
    field = func()
}

def func() {
    ...
    return "value"
}
```

A working example:

{% include file="examples/jenkins/set_environment_by_script.Jenkinsfile" %}

## Comments

I am trying to do something like this and getting error. Can I use conditional assignments in the environment section?

environment{
if (env == "e2e") {
SLACK_CHANNEL = "#e2e-monitoring"
} else if (env == "pqa") {
SLACK_CHANNEL = "#pqa-monitoring"
}
}



<hr>

so beautiful article!!!!

<hr>

Thanks for this tutorial. However, I'm having hard times understanding how to pass environment variables in case of Jenkins Pipelines by NOT using Jenkinsfile. In case of simple Jenkins build projects it was easy to do. However, how can I add custom environment variables to Jenkins Pipeline Multibranch build project so that the variables are not in Jenkinsfile?

I don't want to add sensitive keys, passwords etc to Jenkinsfile that would go to version control system.

Any tips?

---

You can add "secrets" to your Jenkins server and then those secrets will be available to your jobs, but won't be part of your Jenkinsfile.
https://www.jenkins.io/doc/book/using/using-credentials/

---

Thanks! That's what I figured out, too but it's very cumbersome way of doing this:( Right now I went back to old way of creating builds - step by step and I do stuff in "Shell" step where I can set env variables easily.

Strange that some developers came up with that idea that when you add env variables in your pipeline steps these will be written and committed back to your git repo. That's VERY dangerous. Just wondering :)

---

Why would you add the environment variables to your repo? The link I shared does not do that.

---

I would not and as I explained - it's very bad idea.
I tried to explain that the standard way of doing it in the pipelines (add env variables by each step or to the pipeline) is designed in a really bad way so that whatever changes you do to your pipeline in Jenkins - it would get committed to SCM.

I added screenshot to illustrate my problem.

---

I did not see that happening.

<hr>

i'm new in jenkins, i would know if someone know how can i build a remote trigger in the multibranch pipeline with post commit hook ?
and how can i get the current name branch in Pipeline job because i want to do some stages in master branch and other in develop branch
for example when i try with echo env.BRANCH_NAME it's return NULL :(

<hr>

can I make all the environment variables as None before my pipeline starts? and then set few values if I want. Is it possible?


---
I am not sure I understand you. Why would you want to do that? What are you trying to achieve?

The environment variables come from the system, without them probably Jenkins would not be able to run. However you can set the ones you like in your Jenkins file first to be none and then to some interesting value.

---
I am using these env.vars to set few jenkins parameters in my groovy. Because of which they are retaining previous builds parameters. I am trying to find a way to not retain the previous build's values.
---
Jenkins gives you access to some meta data of the previous builds, but you don't need to access them.

What environment variables do you see that come from an earlier build?

---

I am not using any system env variables to set to the parameters. Am setting some parameters to my jenkins job, by doing env.build="yyyyyyy" and am setting the parameters to env.build as default values if its not set in the current build and is none. I see even though am not setting any env.build next time, its value is being taken from the previous build and is set to the jenkjns parameter.

---

Could you create a minimal example that shows this?

---

def string_param(Map opt=[defaultValue:"", description:""]) {

if (opt.name == null) {
throw new Exception("Arg name is mandatory")
}

return string(name: "$opt.name", defaultValue: "$opt.defaultValue",
description: "$opt.description")
}

def def_boards = env."${board_u}_BOARDS"
def boards = string_param(name: "${board}_boards",
defaultValue: "${def_boards?:''}",
description: "Enter $board boards example: abc-1,abc-2")

in the first build when I set, env.xyz_BOARDS="xxxxxxxxxxxxx", for the second build even though am not setting it, this value is being retailed to boards value. How can I stop that for being retained?


---

It is unclear to me why Jenkins keeps the old values, but at the end of your job you could set them to null again to make sure they are clean.

---

Yeah thank you. I tried resetting the vars in the start of the groovy so that it would work for concurrent builds as well and I see its working as intended. Thank you

<hr>
Can you make a article on Jenkins shared libs ?

<hr>

env.first_path

calling a method that way is not something I would want to do too often, it just looks like a field, and it may/can have side-effects. Good explainer of the gotchas , thanks for sharing
:-)





