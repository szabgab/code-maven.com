counter = [0] * 10
fh = new File('examples/data/count_digits.txt')
reader = fh.newReader()
while ((line = reader.readLine()) != null) {
    for (c in line) {
        if (c in ' ') {
            continue
        }
        counter[ c as Integer ]++
    }
}

for (i=0; i<10; i++) {
    println i + ' ' + counter[i]
}


