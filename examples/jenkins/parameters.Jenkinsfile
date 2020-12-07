pipeline {
    agent { label 'master' }
    parameters {
       string(name: 'hostname', defaultValue: 'gabor-dev', description: 'Hostname or IP address')
       booleanParam(name: 'yesno', defaultValue: false, description: 'Checkbox')
       choice(name: 'planet', choices: ['Mercury', 'Venus', 'Earth', 'Mars'], description:  'Pick a planet')
    }
    stages {
        stage('display') {
            steps {
                echo params.hostname
                echo params.yesno
                echo params.
            }
        }
    }
}
