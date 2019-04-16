

def fibo(n) {
    if (n == 1 || n == 2) {
        return 1
    }
    return fibo(n-1) + fibo(n-2)
}

println( fibo(1) )  // 1
println( fibo(2) )  // 1
println( fibo(3) )  // 2
println( fibo(4) )  // 3
println( fibo(5) )  // 5
println( fibo(6) )  // 8
