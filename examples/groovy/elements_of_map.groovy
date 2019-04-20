def colors = [red: '#FF0000', green: '#00FF00', blue: '#0000FF']
println colors
println colors.containsKey('red')
println colors.containsKey('black')

for (p in colors) {
    println p.key
    println p.value
}
