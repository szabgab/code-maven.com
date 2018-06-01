
def a_mess = ["question", 42, 'answer']
println a_mess              // [question, 42, answer]
println a_mess.size()       // 3
println a_mess[0]           // question
println a_mess.getClass()   // class java.util.ArrayList

def names = ['foo', 'bar', 'qux'] as LinkedList
println names               // [foo, bar, qux]
println names.size()        // 3
println names[1]            // bar
println names.getClass()    // class java.util.LinkedList

for (i = 0; i < names.size(); i++) {
   println i + ') ' + names[i]
}
// 0) foo
// 1) bar
// 2) qux


names.each {
    println it
}
// foo
// bar
// qux

names.each { name ->
    println name
}
// foo
// bar
// qux

names.eachWithIndex { name, i ->
    println i +  '] ' + name
}
// 0] foo
// 1] bar
// 2] qux

