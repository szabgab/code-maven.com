import groovy.json.JsonSlurper

def json_str = '''{
   "name": "Foo Bar",
   "year": 2018,
   "timestamp": "2018-03-08T00:00:00",
   "tags": [ "person", "employee" ],
   "grade": 3.14 }'''


def jsonSlurper = new JsonSlurper()
cfg = jsonSlurper.parseText(json_str)
println(cfg)          // [name:Foo Bar, year:2018, timestamp:2018-03-08T00:00:00, tags:[person, employee], grade:3.14]
println(cfg['name'])  // Foo Bar
println(cfg.name)     // Foo Bar
