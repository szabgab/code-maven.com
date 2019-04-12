
def x = 42

def f() {
    // println(x)  // Caught: groovy.lang.MissingPropertyException: No such property: x for class: scope
    def x = 23
    println(x)      // 23
}


f()
println(x)          // 42
