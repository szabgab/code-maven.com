
x = 42

def f() {
    println(x)      // 42
    def x = 23
    println(x)      // 23
}


f()
println(x)          // 42
