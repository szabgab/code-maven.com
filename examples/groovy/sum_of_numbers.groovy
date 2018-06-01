sum = 0

fh = new File('examples/data/numbers.txt')
println fh.getClass()        // class java.io.File

def lines = fh.readLines()

lines.each { line ->
    sum += line as Integer
}

println "The sum is: " + sum   // 126


