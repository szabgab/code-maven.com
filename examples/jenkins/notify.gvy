def notify(status) {
   wrap([$class: 'BuildUser']) {
       emailext (
       subject: "${status}: Job ${env.JOB_NAME} ([${env.BUILD_NUMBER})",
       body: """
       Check console output at <a href="${env.BUILD_URL}">${env.JOB_NAME} (${env.BUILD_NUMBER})</a>""",
       to: "${BUILD_USER_EMAIL}",
       from: 'jenkins@company.com')
   }
}

