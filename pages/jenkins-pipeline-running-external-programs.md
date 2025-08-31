---
title: "Jenkins Pipeline: running external programs with sh or bat"
timestamp: 2018-08-20T21:30:01
tags:
  - sh
  - bat
published: true
books:
  - jenkins
author: szabgab
archive: true
---


From within a Jenkins pipeline you can any external program. If your pipeline will run on Unix/Linux you need to use the `sh` command.
If your pipeline will run on MS Windows you'll need to use the `bat` command.

Naturally the commands you pass to these will also need to make sense on the specific operating system.

In this example first we use the internal `echo` command of Jenkins.

Then we call `sh` and run the `echo` of our Unix shell.

Then we execute the `hostname` command and finally the `uptime` command.


```groovy
pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                echo "Hello World!"
                sh "echo Hello from the shell"
                sh "hostname"
                sh "uptime"
            }
        }
    }
}
```

The result looks like this:

```
Started by user Gabor Szabo
Running in Durability level: MAX_SURVIVABILITY
[Pipeline] node
Running on Jenkins in /var/lib/jenkins/workspace/simple-pipeline
[Pipeline] {
[Pipeline] stage
[Pipeline] { (build)
[Pipeline] echo
Hello World!
[Pipeline] sh
[simple-pipeline] Running shell script
+ echo Hello from the shell
Hello from the shell
[Pipeline] sh
[simple-pipeline] Running shell script
+ hostname
s17
[Pipeline] sh
[simple-pipeline] Running shell script
+ uptime
 17:15:35 up 3 days,  1:59,  0 users,  load average: 0.00, 0.00, 0.00
[Pipeline] }
[Pipeline] // stage
[Pipeline] }
[Pipeline] // node
[Pipeline] End of Pipeline
Finished: SUCCESS
```

## MS Windows

A few examples in Windows:

Show the name of the computer (a bit like hostname on Unix):

```
bat 'wmic computersystem get name'
```

Print out the content of the PATH environment variable as seen by Windows.

```
bat 'echo %PATH%'
```

Of course we could have printed the PATH environment variable without invoking an external call:

```
echo env.PATH
```

## Print out all the environment variables seen by Windows.

```
echo bat(returnStdout: true, script: 'set')
```

## Get the disk size of a local disk

```
script {
    def disk_size = sh(script: "df / --output=avail | tail -1", returnStdout: true).trim() as Integer
    println("disk_size = ${disk_size}")
}
```


Full examples:

{% include file="examples/jenkins/list_disk_size.Jenkinsfile" %}

## Get the disk size of a remote disk

```
script {
    def disk_size = sh(script: "ssh remote-server df / --output=avail | tail -1", returnStdout: true).trim() as Integer
    println("disk_size = ${disk_size}")
}
```

## Comments

I have a pipeline with tests running with maven, how can I get the name of each test run out of the pipeline output?

---

I have a question...I am implementing a pipeline and I m using k8s plugin an run the pipeline in pods and created my own docker container with nessery libraries. My scripts is based on groovy scripts and I am heavly use 'sh' to execute shell commands due to my IaC..in your examples you have used many sh block under one single step.. even though you have the ability to run all things in a one sh block (that a because of You may have used that kind approach to explain the sh Ior you don't care and you use as much as you like..let's assume that you don't care and use many..to understand my concern ). My practice is to handle the control flow with the groovy as much as possible and things I need to do with the shell I used sh blocks inside those groovy control blocks (if else). Since I m prefer to use groovy due to the flexibility. If someone is arguing that when you has the ability to control the flow in same sh block by providing the groovy value with the interpolation in to the shell block as the condition values.. why do you do that in two sh block while maintaining the control flow with groovy. ...for this question my point is when I am having a advanced tool like groovy why don't I consider that as the primary tool and I am using groovy to maintain the control flow and shell is a very low level option and the flexibility is low than groovy and I am arguing that then why don't you write shell script for your entire pipeline.. ..these are two perceptions on sh.. I would like to know you perception on these two aspects... actually what kind of best practice we should follow..

---

In this example I was indeed only showing that you can use "sh" or "bat" to execute external commands.

The external commands can be written in any language, not just shell.

My recommendation is to write as much as you can in some high-level languages (e.g. Perl, Python, Ruby) and make it independent from the fact that it is being executed by Jenkins.

Write the part in Groovy only if must interact with the steps of the Jenklins pipeline.

It is usually easier to write in those languages than in Shell or in Groovy and that will make your code more flexible so people might execute them on their own system without using Jenkins.

---

what if i have to migrate that shell script into Jenkins itself. Is there a way to just use that shell script in Jenkins?

---

What do you mean "into Jenkins itself"?

---
So i am using an external shell script which is located on my Jenkins server. I have to give up my server and migrate Jenkis to a POD on openshift. Is there a way to import that file in the Jenkis itself and use it in the jobs using a plugin or something?

---
You could have the shell script embedded in the Jenkins file and then save it and run it when needed, but it is a nasty hack. I would recommend that both your Jenkinsfile and your shell script were in some version control system that is then cloned when Jenkins runs the job.

---

would it be possible to call a batch file and still continue with other commands with the same 'bat' block...? Something like bat ''' mybatchfile.bat
pip install mypackage '''.

The use case would be to activate a created python virtual environment and to continue installing packages within that virtual environment.
In this case, if I want to activate a python virtual environment, I am supposed to call a batch file (activate.bat) and then I should continue with the 'pip install my-python-package'

---

I think what you mean is running the external process in the background. On windows you'd use START for this. On Linux/OSX you would put & at the end of the command.

---

how can i use a curl command in jenkins pipeline where the node is windows?

---

How can you use curl on Windows without Jenkins?

---

Hi, I want to download the file using wget and check if the file is available using shell script in pipeline. How do i do that?
Im trying something like below but it is failing syntactically. Im new to groovy.

sh """
status=$(curl --head --silent ${REPO_URL} | head -n 1) ---Failing in this line
if echo ${status} | grep -q 404
echo 'No previous versions for the components exists'
else
gunzip ${FILE_NAME}.tar.gz
tar -xvf ${FILE_NAME}.tar
def props = readProperties file:'component.properties'
PREVIOUS_DATALOAD_VERSION = props['PREVIOUS_DATALOAD_VERSION']
PREVIOUS_SERVER_VERSION = props['PREVIOUS_SERVER_VERSION']
fi
"""

---
why are you mixing groovy code in shell script? Line:8

