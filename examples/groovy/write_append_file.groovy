File file = new File("out.txt")
file.write("first\n")
file.append("second\n")
file.write("third\n")

println file.text
