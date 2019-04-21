
def sqrt(int n) {
    if (n < 0) {
        throw new Exception("The number ${n} was negative")
    }
    return Math.sqrt(n)
}


println( sqrt( 4 ))    // 2.0
println( sqrt( -1 ))   // exception
println('still alive') // is not executed...
