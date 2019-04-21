def div(a, b) {
    return a/b
}



if (args.size() < 2) {
    println("You need to pass two numbers")
    System.exit(1)
}


try {
    def res = div(args[0] as Integer, args[1] as Integer)
    println(res)
} catch(Exception e) {
    println("Exception: ${e}")
}

