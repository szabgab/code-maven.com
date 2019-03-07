import java.text.SimpleDateFormat
pipeline {
   agent none
   options {
       ansiColor('xterm')
       timestamps()
   }
   parameters {
       string(name: 'machine', defaultValue: '', description: 'Name of the machine')
       string(name: 'size',   defaultValue: '23', description: 'The size')
       choice(choices: ['Mercury', 'Venus', 'Earth', 'Mars'], description:  'Pick a planet', name: 'planet')
   //}
   stages {
       stage('try') {
           agent { label 'master' }
           steps {
               script {
                   sh "hostname"

                   def data = readJSON text: '{}'
                   data.name = "test-529" as String
                   data.date = new java.text.SimpleDateFormat('yyyyMMddHHmmss').format(new Date())
                   writeJSON(file: 'mydata.json', json: data, pretty: 4)
                   archiveArtifacts artifacts: 'mydata.json', onlyIfSuccessful: true

                   //error("Fail after first artifact")

                   writeJSON(file: 'otherfile.log', json: data, pretty: 4)
                   archiveArtifacts artifacts: '*.log', onlyIfSuccessful: true
               }
           }
       }
   }
}

