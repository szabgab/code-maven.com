Random random = new Random()
def hidden = random.nextInt(20)

while (true) {
    print "Guess number: "
    def guess = System.in.newReader().readLine() as Integer
    if (guess < hidden) {
        println "Guess was too small"
    } else if (guess > hidden) {
        println "Guess was too hight"
    } else {
        println "Match!"
        break
    }
}

println "Bye"
