import groovy.json.JsonOutput

if (args.size() < 1) {
    println("Missing filename")
    System.exit(1)
}

filename = args[0]


def data = [
    name: "Foo Bar",
    year: "2018",
    timestamp: "2018-03-08T00:00:00",
    tags: [ "person", "employee"],
    grade: 3.14
]

def json_str = JsonOutput.toJson(data)
def json_beauty = JsonOutput.prettyPrint(json_str)
File file = new File(filename)
file.write(json_beauty)
