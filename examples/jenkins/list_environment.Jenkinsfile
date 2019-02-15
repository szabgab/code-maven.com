pipeline {
   agent none
   environment {
       color = "blue"
   }
   stages {
       stage('first') {
            agent { label 'master' }
            steps {
               sh "printenv | sort"
            }
        }
    }
}

