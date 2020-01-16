
def specificCause = currentBuild.getBuildCauses('hudson.model.Cause$UserIdCause')
if (specificCause) {
    println("Executed by user $specificCause.userName")
    //echo "specificCause: $specificCause"
    //echo "specificCause: ${specificCause.userId[0]}"
    echo "specificCause: $specificCause.userName"
    echo "specificCause: ${specificCause.userName}"
    //echo "specificCause: $specificCause.shortDescription"
}
