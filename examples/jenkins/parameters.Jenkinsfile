pipeline {
    agent { label 'master' }
    parameters {
       string(name: 'hostname', defaultValue: 'gabor-dev', description: 'Hostname or IP address')
       booleanParam(name: 'yesno', defaultValue: false, description: 'Checkbox')
       choice(name: 'planet', choices: ['Mercury', 'Venus', 'Earth', 'Mars'], description:  'Pick a planet')
       text(name: 'story', defaultValue: 'One\nTwo\nThree\n', description: '')
    }
    stages {
        stage('display') {
            steps {
                echo params.hostname
                echo params.yesno ? "yes" : "no"
                echo params.planet
                echo params.story
            }
        }
    }
}

