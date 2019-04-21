
def sqrt(int n) {
    if (n < 0) {
        throw new Exception("The number ${n} was negative")
    }
    return Math.sqrt(n)
}


println( sqrt( 4 ))    // 2.0
try {
   println( sqrt( -1 ))
} catch(Exception e) {
    println("Exception: ${e}")
}                      // Exception: java.lang.Exception: The number -1 was negative
println('still alive') // still alive
