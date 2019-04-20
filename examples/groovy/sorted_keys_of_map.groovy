def colors = [red: '#FF0000', green: '#00FF00', blue: '#0000FF']

for (key in colors.keySet().sort()) {
    println(key)
    println(colors[key])
}
