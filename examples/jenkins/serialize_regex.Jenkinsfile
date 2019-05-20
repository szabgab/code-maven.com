pipeline {
    agent { label 'master' }
    stages {
        stage('first') {
            steps {
                script {
                    echo "in first"
                    def text = """This is some long test
                    with more than 1
                    rows.
                    """
                    def match = (text =~ /\bsome\b/)
                    println("still first")
                    check_me()
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
        }
        failure {
            echo "in post failure"
        }
    }
}

def check_me() {
    println("in check")
    def text = """This is some long test
        with more than 1
        rows.
    """
    def match = (text =~ /\bsome\b/)
}


