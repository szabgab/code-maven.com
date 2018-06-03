filename = 'examples/data/count_digits.txt'

// read all the content of the file into a single string
File fh1 = new File(filename)
text = fh1.getText('UTF-8')

// read all the lines into a list, each line is an element in the list
File fh2 = new File(filename)
def lines = fh2.readLines()
for (line in lines) {
    // ...
}


File fh3 = new File(filename)
LineNumberReader reader = fh3.newReader()
while ((line = reader.readLine()) != null) {
    // ...
}
