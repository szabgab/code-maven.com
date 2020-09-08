pipeline {
    agent {
        label 'master'
    }
    parameters {
        string(name: 'text',              defaultValue: 'Some Text',  description: 'Text')
        string(name: 'foreground_color',  defaultValue: 'black',      description: 'Foreground')
        string(name: 'background_color',  defaultValue: 'lightgreen', description: 'Background')
        string(name: 'border_size',       defaultValue: '5px',        description: 'Border size')
        string(name: 'border_color',      defaultValue: 'yellow',     description: 'Border color')
    }

    stages {
        stage('Check disk usage') {
            steps {
                script {
                    manager.addShortText(
                        params.text,
                        params.foreground_color,
                        params.background_color,
                        params.border_size,
                        params.border_color
                    )
                    currentBuild.description = "Foreground: ${foreground_color}<br>"
                    currentBuild.description += "Background: ${background_color}<br>"
                    currentBuild.description += "Border size: ${params.border_size}<br>"
                    currentBuild.description += "Border color: ${params.border_color}"

                }
            }
        }
    }
}

