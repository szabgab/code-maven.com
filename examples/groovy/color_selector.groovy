colors = ['Blue', 'Yellow', 'Brown', 'White']

println 'Please select a number:'
colors.eachWithIndex { name, i ->
    println "${i}) ${name}"
}
def selection = System.in.newReader().readLine() as Integer
if (selection < colors.size()) {
    println colors[selection]
} else {
    println "Bad Selection"
}
