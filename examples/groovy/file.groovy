
if (args.size() < 1) {
    println("Missing filename")
    System.exit(1)
}

name = args[0]

fh = new File(name)
println("file      : " + fh.isFile())
println("dir       : " + fh.isDirectory())
println("executable: " + fh.canExecute())
