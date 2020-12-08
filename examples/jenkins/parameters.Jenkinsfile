
pipeline {
    agent { label 'master' }
    parameters {
       string(name: 'hostname', defaultValue: 'gabor-dev', description: 'Hostname or IP address')
       booleanParam(name: 'yesno', defaultValue: false, description: 'Checkbox')
       choice(name: 'planet', choices: ['Mercury', 'Venus', 'Earth', 'Mars'], description:  'Pick a planet')
       choice(name: 'space', choices: ['', 'Mercury', 'Venus', 'Earth', 'Mars'], description:  'Pick a planet. Defaults to empty string')
       text(name: 'story', defaultValue: 'One\nTwo\nThree\n', description: '')
       password(name: 'secret', defaultValue: '', description: 'Type some secret')

    }
    stages {
        stage('display') {
            steps {
                echo params.hostname
                echo params.yesno ? "yes" : "no"
                echo params.planet
                echo params.space
                echo params.story
                //echo params.secret
                echo "--------"
                echo "${params.hostname}"
                echo "${params.yesno}"
                echo "${params.planet}"
                echo "${params.space}"
                echo "${params.story}"
                echo "${params.secret}"
                script {
                    sh "echo ${params.secret}"
                }
            }
        }
    }
}

