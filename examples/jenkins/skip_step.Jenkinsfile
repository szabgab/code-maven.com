pipeline {
   agent none
   options {
       ansiColor('xterm')
       timestamps()
   }
   parameters {
       booleanParam(defaultValue: false, description: 'Checkbox', name: 'yesno')
   }
   stages {
       stage('first') {
           agent { label 'master' }
           steps {
               script {
                   println("first before")
                   println(params.yesno)
                   done = true
                   return
                   println("first after")
               }
           }
       }
       stage('second') {
           agent { label 'master' }
           when {
               expression {
                  return ! done;
               }
           }
           steps {
               script {
                   println("second")
               }
           }
       }
   }
}

