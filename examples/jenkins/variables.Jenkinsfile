pipeline {
   agent none
   stages {
       stage('try') {
           agent { label 'master' }
           steps {
               script {
                   //some_strange_name = null
                   //print(some_strange_name)
                   if (true) {
                       print("creating variable")
                       some_strange_name = 1
                   }
                   print(some_strange_name)

                   if (binding.hasVariable('some_strange_name')) {
                       print("has some_strange_name")
                       print(some_strange_name)
                   } else {
                       print("DOES NOT have some_strange_name")
                   }
               }
           }
       }
       stage('try again') {
           agent { label 'master' }
           steps {
               script {
                   if (binding.hasVariable('some_strange_name')) {
                       print("has some_strange_name")
                       print(some_strange_name)
                   } else {
                       print("DOES NOT have some_strange_name")
                   }
               }
           }
       }
   }
}

