#!/bin/bash

JENKINS_URL=$1
NODE_NAME=$2
NODE_HOME='/home/build/jenkins-node'
EXECUTORS=1
SSH_PORT=22
CRED_ID=$3
LABELS=build
USERID=${USER}

cat <<EOF | java -jar ~/bin/jenkins-cli.jar -s $1 create-node $2
<slave>
  <name>${NODE_NAME}</name>
  <description></description>
  <remoteFS>${NODE_HOME}</remoteFS>
  <numExecutors>${EXECUTORS}</numExecutors>
  <mode>NORMAL</mode>
  <retentionStrategy class="hudson.slaves.RetentionStrategy$Always"/>
  <launcher class="hudson.plugins.sshslaves.SSHLauncher" plugin="ssh-slaves@1.5">
    <host>${NODE_NAME}</host>
    <port>${SSH_PORT}</port>
    <credentialsId>${CRED_ID}</credentialsId>
  </launcher>
  <label>${LABELS}</label>
  <nodeProperties/>
  <userId>${USERID}</userId>
</slave>
EOF
