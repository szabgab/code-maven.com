
pipeline {
    agent { label 'master' }
    stages {
        stage('only') {
            steps {
                script {
                    println("BEFORE")
                    results = []
                    try {
                        def result = build job: "experiment-subproject", wait: true
                        println(result) // org.jenkinsci.plugins.workflow.support.steps.build.RunWrapper
                        println(result.getId())
                    } catch(err) {
                        println("ERROR caught")
                        println(err) // hudson.AbortException: experiment-subproject #4 completed with status FAILURE (propagate: false to ignore)
                        // https://javadoc.jenkins-ci.org/hudson/AbortException.html
                        println(err.getMessage())
                        println(err.getStackTrace())
                        println(err.getCause())
                        println(err.getLocalizedMessage())
                        println(err.toString())
                    }
                    println("AFTER")

                    def res = build job: "experiment-subproject", wait: false
                    println(res) // null

                    rep = build job: "experiment-subproject", wait: true, propagate: false
                    println(rep) // org.jenkinsci.plugins.workflow.support.steps.build.RunWrapper
                    println(rep.getId())
                    println(rep.getResult()) // FAILURE
                    println(rep.getDurationString())
                    results.push(rep)

                    //sh "ls -l"
                    //println("two")
                    //} catch(ArrayIndexOutOfBoundsException ex) {
                    //println("Catching the Array out of Bounds exception");
                    //}catch(Exception ex) {

                    //println("three")
                    //print("A disk image was created: jenkins-agent-1554 and then more")
                    //is_it_the_answer(42)
                    //echo "try again"
                    //try {
                    //    is_it_the_answer(23)
                    //} catch (err) {
                    //   print(err)
                    //    print(err.getMessage())
                    //}
                }
            }
        }
        stage('second') {
            steps {
                script {
                    echo "hi"
                    println(rep.getId())
                    println(rep.getResult()) // FAILURE
                    println(rep.getProjectName())
                    println(rep.getDisplayName())

                    def res = build job: "experiment-subproject", wait: true, propagate: false
                    results.push(res)

//                    if (manager.logContains("three")) {
//                        manager.addWarningBadge("tres")
//                    } else {
//                        manager.addWarningBadge("nem harom")
//                    }
                    //def image_name = ''
                    //def matcher = manager.getLogMatcher(/.* (jenkins-agent-(\d+)).*/)
                    //print(matcher)
                    //if (matcher?.matches()) {
                    //    image_name = matcher.group(1)
                    //    println(image_name)
                    //    manager.addShortText(image_name)
                    //    println(image_name.getClass())
                    //}
                    //do_sg(image_name)
                }
            }
        }
        stage ('gitz') {
            agent { label 'build-small' }
            steps {
                script {
                    results.each {
                         println(it)
                         println(it.getId())
                         println(it.getResult()) // FAILURE
                         println(it.getProjectName())
                         println(it.getAbsoluteUrl())
                    }
                }
            }
        }
    }
}

def is_it_the_answer(n) {
    if (n == 42) {
        return 'yes'
    }
    throw new Exception('Nope')
}

def do_sg(name) {
    print("do_sg with $name")
}
