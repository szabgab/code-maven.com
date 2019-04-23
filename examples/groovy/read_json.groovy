import groovy.json.JsonSlurper

if (args.size() < 1) {
    println("Missing filename")
    System.exit(1)
}

filename = args[0]

def jsonSlurper = new JsonSlurper()
data = jsonSlurper.parse(new File(filename))

println(data)
