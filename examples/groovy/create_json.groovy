def data = [
    name: "Foo Bar",
    year: "2018",
    timestamp: "2018-03-08T00:00:00",
    tags: [ "person", "employee"],
    grade: 3.14
]

println(data["name"])

def json_str = JsonOutput.toJson(data)
print(json_str)

