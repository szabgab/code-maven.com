
root = '../data/dependencies/'

def list_dependencies(name) {
    def path = root + name + '.txt'
    def fh = new File(path)
    if (! fh.exists()) {
        return
    }

    def reader = fh.newReader()
    while ((line = reader.readLine()) != null) {
        println(line)
        list_dependencies(line)
    }
}

list_dependencies('main')

