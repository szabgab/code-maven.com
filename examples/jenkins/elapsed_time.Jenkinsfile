import groovy.time.TimeCategory
import groovy.time.TimeDuration

pipeline {
    agent { label 'master' }
    stages {
        stage('first') {
            steps {
                script {
                    start = new Date()
                    echo "in first"
                }
            }
        }
        stage('second') {
            steps {
                script {
                    echo "in second"
                }
            }
        }
    }
    post {
        always {
            echo "in post always"
            script {
                def stop = new Date()
                TimeDuration td = TimeCategory.minus( stop, start )
                println("Elapsed time: $td")
            }

        }
        failure {
            echo "in post failure"
        }
    }
}

