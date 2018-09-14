def add = { x, y ->
   //println('add')
   return x+y
}

def multiply = { x, y ->
   //println('multiply')
   return x*y
}


def calc(a, b, f) {
   //println('calc')
   println(f(a, b))
}

calc(4, 5, add)
calc(4, 5, multiply)
