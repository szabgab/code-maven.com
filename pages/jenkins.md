---
title: "Jenkins"
timestamp: 2018-03-24T07:30:01
tags:
  - Jenkins
  - Devops
published: true
author: szabgab
archive: true
show_related: false
---


[Jenkins](https://jenkins.io/) is an automation server. It allows for all kinds of automations. It is primarily used for Build automation, Continuous Integration, and Continuous Deployment.


## Installations

<ol>
    <li>[Install Jenkins on Ubuntu](/install-jenkins-on-ubuntu) (using Vagrant)</li>
    <li>[Vagrant for Jenkins on Ubuntu](/vagrant-for-jenkins-on-ubuntu)</li>
    <li>[Jenkins in Docker](/jenkins-in-docker)</li>
</ol>

## Examples

<ol>
    <li>[Jenkins Pipeline - Hello World](/jenkins-pipeline-hello-world) (pipeline, agent, stages, stage, stpes, echo)</li>
    <li>[Jenkins Pipeline: running external programs with sh or bat](/jenkins-pipeline-running-external-programs), returnStdout, trim</li>
    <li>[Jenkins Pipeline: Send e-mail notifications](/jenkins-send-email-notifications)</li>
    <li>[Jenkins Pipeline: Add some text to the job using manager.addShortText](/jenkins-pipeline-short-text)</li>
    <li>[Jenkins CLI: create node](/jenkins-cli-create-node)</li>
    <li>[Jenkins Pipeline BuildUser plugin](/jenkins-pipeline-builduser)</li>
    <li>[Jenkins Pipeline - set and use environment variables](/jenkins-pipeline-environment-variables)</li>
    <li>[Jenkins Pipeline: git checkout using reference to speed up cloning large repositories](/jenkins-git-check-out-using-reference)</li>
    <li>[Jenkins report the name of the stage that failed](/jenkins-report-failed-stage-name) (STAGE_NAME)</li>
    <li>[Jenkins Pipeline: triggers from Version Control Systems](/jenkins-triggers) (pollSCM)</li>
    <li>[How to set the job number and description for a Jenkinsfile in a Jenkins Pipeline?](/jenkins-pipeline-set-job-name-and-description) (currentBuild, displayName, description)</li>
    <li>[Jenkins Pipeline: read a file, write a file - readFile, writeFile](/jenkins-readfile-writefile)</li>
    <li>[Separate jobs for development and production](/jenkins-separate-jobs-for-development-and-production) currentBuild, projectName</li>
    <li>[Jenkins pipeline: get current user](/jenkins-get-current-user) (currentBuild, getBuildCauses)</li>
    <li>[Jenkins parameters](/jenkins-pipeline-parameters)</li>
    <li>[Arbitrary code execution in the shell](/jenkins-arbitrary-code-execution) (sh, parameters)</li>
    <li>[Jenkins pipeline: parallel stages](/jenkins-pipeline-parallel-stages)</li>
    <li>[Jenkins Pipeline: Collect exit code from external commands](/jenkins-pipeline-collect-exit-code-from-external-commands) (sh, bat, returnStatus)</li>
    <li>[Jenkins pipeline: Get previous build status - currentBuild, getPreviousBuild](/jenkins-pipeline-get-previous-build-status)</li>
    <li>[Jenkins pipeline: interactive input during process](/jenkins-pipeline-interactive-input-during-process) (input)</li>
    <li>[Jenkins pipeline: List agents by name or by label](/jenkins-pipeline-list-agents-by-name-or-by-label)</li>
    <li>[Jenkins pipeline: add badges](/jenkins-pipeline-add-badges)</li>
    <li>Report failures.</li>
    <li>Send alerts</li>
    <li>Collect test coverage data.</li>
    <li>[Jenkins slides](/slides/jenkins/)</li>
    <li>[Jenkins printing Unicode characters](/jenkins-pipeline-unicode)</li>
</ol>

## Run external code, capture output

```
script {
      v = sh(script: 'echo " 42"; echo', returnStdout: true).trim()
      echo v
      echo "a${v}b"
}
```

`bat` for windows.

## catch and print error in jenkins

jenkins exception try - catch

https://fraaargh.wordpress.com/2018/06/20/get-a-jobs-console-logfile-from-a-jenkins-pipeline/

```
pipeline {
   agent none
   stages {
       stage ('Catch crash') {
           agent { label 'master'}
           steps {
               echo "before crash"
               script {
                   try {
                       sh 'exit 1'
                   } catch (err) {
                       echo "exception caught, going on"
                       println err // java.lang.ClassCastException:
org.jenkinsci.plugins.workflow.steps.EchoStep.message expects class java.lang.String but received
class hudson.AbortException
                   }
               }
               echo "after crash"
           }
       }
       stage ('Continue after crash') {
           agent { label 'master'}
           steps {
               echo "stage after crash"
           }
       }
   }
}
```

```
                    try {
                        //sh "ls -l no_such"
                        a = 10
                        b = 0
                        c = a/b
                    }
                    catch(Exception ex) {
                         //currentBuild.result = 'FAILURE'
                        println("exception")
                        println(ex) // hudson.AbortException: script returned exit code 2
                        println(ex.toString())
                        println(ex.getMessage())
                        println(ex.getStackTrace())
                    }
```


## dir and tmp are problematic

```
  stages {
       stage ('Run external exe') {
           agent { label 'master'}
           steps {
               sh 'pwd'
               dir('/tmp/gabor') {
                   echo "inside"
                   sh 'pwd'
                   //sh 'sudo ./do-something.py'
               }
               sh 'pwd'
               //sh "sudo sh -c 'cd /tmp; ./do-something.py; cd -'"
           }
       }
```

{% include file="examples/jenkins/mkdir_exception.txt" %}

## Jenkins / Groovy -  define functions and call them with parameters

```
def report(status) {
   println "status=${status}"
}
```

and call them

```
report("text")
```

## Environment variables on Linux

```
sh 'printenv'
sh 'env'
```

## git Backup

[gist](https://gist.github.com/cenkalti/5089392)


## Other

```
echo bat(returnStdout: true, script: 'set')

build(job: 'RevertServerAutomationCloud', parameters: [
     string(name: 'VM_SNAPSHOT', value: 'CleanDb')
])
```

how to include one jenkinsfile in another one?

how to avoid repetititon?


```
stage('Revert agent 100')
         {
             steps
                     {
                     }
         }

 stage('Revert agent 102')
         {
             steps
                     {

                     }
         }
```

how do try - catch and repeat interact?

```
vSphere buildStep: [$class: 'RevertToSnapshot', snapshotName: "${params.VM_SNAPSHOT}", vm: "${params.VM_NAME}"], serverName: '192.168.1.1'

httpRequest authentication: 'df8-b86d-3272', consoleLogResponseBody: true, httpMode: 'POST', ignoreSslErrors: true, responseHandle: 'NONE', url:
"http://192.168.1.1:8080/computer/${params.AGENT_NAME}/doDisconnect?offlineMessage=bye", validResponseCodes: '100:404'
```


## Active Choices Parameter

{% include file="examples/jenkins/array_list.txt" %}

## Options

```
   options {
       ansiColor('xterm')
       timestamps()
   }
```

## Scripts

<strong>Scripts not permitted to use method groovy.lang.GroovyObject invokeMethod java.lang.String java.lang.Object
(org.jenkinsci.plugins.workflow.cps.EnvActionImpl keys). Administrators can decide whether to approve or reject this
signature.</strong>


## archiveArtifacts can be called multiple times

```
archiveArtifacts artifacts: 'mydata.json', onlyIfSuccessful: true
writeJSON(file: 'otherfile.log', json: data, pretty: 4)
archiveArtifacts artifacts: '*.log', onlyIfSuccessful: true
```


## Environment variable values must either be single quoted, double quoted, or function calls.

They cannot be earlier defined environment variables or parameter values.
We can however overcome this limitation by calling a function and passing the values to it.

{% include file="examples/jenkins/exceptions.jenkinsfile" %}

## Jenkins environment

Even if there is an exception in the environment section Jenkins will still run the "success" part of the post section.
Same problem if there is an exception on one of the functions.

To overcome this we create an environment variable as the last step in the environment section
and then we check that variable using

if (! binding.hasVariable('environment_is_set')) {
       error("Environment failed to set properly")
}


That does not help in case there is an exception in the functions.



## http_request

```
response = httpRequest discovery_url
println response
config_str = response.getContent()
for (item in config.sources) {
  item.value
  item.key
```

## Sending e-mail problem fixed

https://stackoverflow.com/questions/20188456/how-to-change-the-security-type-from-ssl-to-tls-in-jenkins

* Sending e-mail
 In Manage Jenkins - Configure System in the
    Extended mail section set the
       SMTP:  smtp.office365.com
       Domain name: @company.com
         Advanced:
             Use SMTP Authentication: +
             User Name: cicdserver@company.com
             Password:              SMTP port: 587
    E-mail notification section:
        SMTP server: smtp.office365.com
    Default user e-mail suffix: @company.com
        Advanced
              User Name: cicdserver@company.com
              Password:               SMTP port: 587


 Shut down Jenkins (via the Windows services)
 Open the file: C:\Program Files (x86)\Jenkins\jenkins.xml
 and change the arguments line to be:

{% include file="examples/jenkins/arguments.txt" %}

 (specifically add:  -Dmail.smtp.starttls.enable=true  )
 Then start Jenkins again.


Client was not authenticated to send anonymous mail
Error sending to the following VALID addresses

{% include file="examples/jenkins/variables.Jenkinsfile" %}


## Skip steps

Jenkins pipeline stop early with success
How to indicate that a job is successful
[pipeline conditional step stage](https://stackoverflow.com/questions/37690920/jenkins-pipeline-conditional-step-stage)

{% include file="examples/jenkins/skip_step.Jenkinsfile" %}

{% include file="examples/jenkins/worker_job.Jenkinsfile" %}


## jenkins sh commnad fails - jenkins stops

{% include file="examples/jenkins/sh_fails.jenkinsfile" %}



## Repository branch filter for Git

It will start multiple jobs if more than one branch was pushed out.
It is triggered even if there were no new commits in the branch that was pushed out

By default it will run every branch matching the filter, even if that branch was last changed 2 years ago.
This can be a problem if for some reason your have hundreds or thousands of historical branches.

```
:^origin/(work|dev)-.*
```

You can limit this by selecting another option and setting the ancestry date to limit how many days
you are ready to go back in time.

* Strategy for choosing what to build
* Choosing strategy: Ancestry
* Maximum Age of Commit: 1

In a pipeline

{% include file="examples/jenkins/branch_filter_age_limit.jenkinsfile" %}

## Jenkins Pipeline code reuse

https://cleverbuilder.com/articles/jenkins-shared-library/
https://jenkins.io/doc/book/pipeline/shared-libraries/

## Exceptions

When you encounter one of those 40-lines long Java stack-traces, look for <b>WorkflowScript</b> to locate the source of the problem.

{% include file="examples/jenkins/exception_catching.jenkinsfile" %}

## Jenkins parse console output


The <b>logContains</b> can parse the log created be the previous stages (but not the current stage)
It can also be used in a post-action.

"manager" is org.jvnet.hudson.plugins.groovypostbuild.GroovyPostbuildRecorder$BadgeManager@41fe3861

[Postbuild plugin](https://wiki.jenkins.io/display/JENKINS/Groovy+Postbuild+Plugin)

{% include file="examples/jenkins/parse_console_output.jenkinsfile" %}

## readJSON

[no such dsl method](https://stackoverflow.com/questions/46841877/java-lang-nosuchmethoderror-no-such-dsl-method-readjson)

## jenkins build step

https://jenkins.io/doc/pipeline/steps/pipeline-build-step/

jenkins collect status from invoked jobs

{% include file="examples/jenkins/status_from_build.Jenkinsfile" %}

## links

https://jenkins.io/doc/pipeline/steps/

https://jenkins.io/doc/pipeline/steps/pipeline-build-step/#-build-%20build%20a%20job

https://jenkins.io/doc/pipeline/steps/pipeline-input-step/


```
               script {
                    manager.addShortText("\n${params.cluserName}", "black", "yellow", "0px", "white")
                    manager.addShortText("${params.clusterId}-${params.command}", "black", "lightgreen", "0px", "white")
                    manager.addShortText("${params.services}", "black", "AliceBlue", "0px", "white")
                    if (params.usage) {
                        manager.addShortText("${params.usage}", "DimGray", "AliceBlue", "0px", "white")
                    }
                }
```


## Elapsed time

{% include file="examples/jenkins/elapsed_time.Jenkinsfile" %}


## Serialize regex

After a regex matching Jenkins sometimes wants to serialize the object, but it cannot do it and thus is raises an
exception. (I have not yet figured out when does this happen.)

{% include file="examples/jenkins/serialize_regex.Jenkinsfile" %}

## Send mail

```
emailext (
    subject: "Test by Gabor",
    body: "Test from Gabor",
    to: 'foo@bar.com',
    from: 'jenkins-noreply@example.com',
    listId: 'gabor-experimental',
)
```


## Jenkins - check if host is accessible

{% include file="examples/jenkins/ping_host.jenkinsfile" %}

## last started stage

```
//   last_started = env.STAGE_NAME
```

## Early stop

jenkins - skip rest of the current stage, early end of current stage  - stop the whole job reporting error

```
return  // skipping rest of the current stage, running next stage
error("Some error message")  // raise an exception stop the whole job
```

## currentBuild

```
echo currentBuild.number  // failed expecting number
println(currentBuild.number)  // works

println("Number: ${currentBuild.number}")
println("Result: ${currentBuild.result}")
println("Display name: ${currentBuild.displayName}")
```

during the steps the result is null
in the post section it is already 'SUCCESS' or 'FAILURE'

[getting started](https://jenkins.io/doc/book/pipeline/getting-started/)


## returnStatus instead of stopping the job

the exit code

```
def res2 = sh(script: "pwd", returnStatus: true)
```


## Sample code

```
def errors = ''
def res = 'SUCCESS'
def res1 = sh(script: "xyz", returnStatus: true)
println("res1 ${res1}")
if (res1 !=0) {
    res = 'FAILURE'
    errors += "xyz"
}
def res2 = sh(script: "abc", returnStatus: true)
println("res2: ${res2}")
if (res2 !=0) {
    res = 'FAILURE'
    errors += "abc"
}
def res3 = sh(script: "pwd", returnStatus: true)
println("res3: ${res3}")
if (res3 !=0) {
    res = 'FAILURE'
    errors += "pwd"
}
//if (params.expected == 'Success') {
//    sh "pwd"
//} else {
//    sh "xyz"
//}
if (res == 'FAILURE') {
    error(errors)
```



## jenkins error, we need to clean the regex variables

```
def output = sh(...)
def version = (output =~ /Version\s*:\s*([\d.]+)/)
def build_number = (output =~ /Build number\s*:\s*([\d]+)/)
currentBuild.description = "${version[0][1]} - ${build_number[0][1]}<br>"
version = ""
build_number = ""
```


## Optional artifacts

```
post {
    always {
        script {
            archiveArtifacts artifacts: 'screenshots/*', fingerprint: true, allowEmptyArchive: true
        }
    }
}
```

[archiveArtifacts](https://www.jenkins.io/doc/pipeline/steps/core/)


[schedule](https://stackoverflow.com/questions/34594703/add-build-parameter-in-jenkins-build-schedule)


## multiple cron with parameter

{% include file="examples/jenkins/multiple_cron.Jenkinsfile" %}
