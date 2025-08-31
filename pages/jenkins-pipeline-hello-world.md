---
title: "Jenkins Pipeline - Hello World"
timestamp: 2018-08-20T20:30:01
tags:
  - pipeline
  - stages
  - stage
  - step
  - echo
  - agent
  - master
  - slave
  - node
published: true
books:
  - jenkins
author: szabgab
archive: true
---


Let's create our first Jenkins Pipeline. Without any actual software, just printing "Hello World".


Aftr logging in to Jenkins click on the "New Item" menu option:

<img src="/img/jenkins-menu.png" alt="Jenkins Menu" />


Type in the name of the Jenkins Pipeline (simple-pipeline in our case).

Click on the "Pipeline".

Then press the "OK" button. (It will be disabled until you select a project-type)

<img src="/img/jenkins-new-item.png" alt="Jenkins New Item" />

It will take you directly to the "Configuration" page of the project that looks like this:

<img src="/img/jenkins-pipeline-config.png" alt="Jenkins Pipeline config" />

Scroll down to the section called "Pipeline", paste the following code:


```
pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                echo "Hello World!"
            }
        }
    }
}
```

It will look like this:

<img src="/img/jenkins-hello-world-pipeline.png" alt="Jenkins Pipeline" />

Click on "Save".

It will take to the menu of the specific project:

<img src="/img/jenkins-pipeline-menu.png" alt="Jenkins Pipeline menu" />

Click on the "Build Now" button.

It will start running the pipeline and within a few seconds you'll see an indicator of your first job
being successful (blue dot on the left hand side).

<img src="/img/jenkins-pipeline-first-build.png" alt="Jenkins First job" />

If you click on that blue dot on the left hand side it will take you to the "Console Output" that looks like this:

<img src="/img/jenkins-hello-world-console.png" alt="Jenkins Console output" />

## What is in the first pipeline?

You can see the basic structure of the pipelines.

Everything is wrapped in a block called "pipeline". Inside we need to declare on which agents can the pipeline run.
In this example we requested it to run on the Jenkins "master". Usually only very small setups rely on the "master".
Once your project starts to grow you'll start setting up agents Later we'll see how to set up agents and how to tell
the different parts of the pipeline to run on different agents. (Originally these were called "slaves". While they are
being renamed to "agents" you'll still find a lot of examples using the word "slave". In some places thet are also called
"nodes". In the end they refer to the same things. Maybe the right way to think about them is that nodes = master + agents,
but then in the pipeline we also call "master" to be an agent. Go figure.

Inside the `pipeline` there can be `stages` (We have one). Inside the `stages` The can be several `stage`
element. Inside each `stage` there must be `steps`. The steps themselves are Jenkins commands.

`echo` will just print something on the console. It can be useful for displaying values as the pipeline makes progress.



