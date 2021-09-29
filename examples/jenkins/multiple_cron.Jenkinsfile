
// multiple cron with parameter

// There is a plugin and this experiment

    triggers {
        cron("35,36 * * * *")
    }

    stages {
        stage('Check disk usage') {
            steps {
                script {
                    echo "--------------"
                    echo "HELLO $BUILD_NUMBER"
                    echo "--------------"
                    String[] ENVS   = ["env1", "env3"]
                    def ENV_COUNT   = ENVS.length
                    def x           = BUILD_NUMBER.toInteger() % ENV_COUNT
                    echo x.toString()
                    echo ENVS[x]

