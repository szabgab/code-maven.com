
def fact(n) {
    if (n == 1) {
       return 1
    }
    return n * fact(n-1)
}

println( fact(5) )  //     120
println( fact(10) ) // 3628800

