sum = 0

fh = new File('examples/data/numbers.txt')
reader = fh.newReader()
println reader.getClass()  // class java.io.LineNumberReader

while ((line = reader.readLine()) != null) {
    sum += line as Integer
}

println "The sum is: " + sum   // 126
