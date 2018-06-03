File file = new File("out.txt")
file.write "First line\n"
file << "Second line\n"

println file.text
