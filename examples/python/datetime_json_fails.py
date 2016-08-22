import json
import datetime

d = {
   'name' : 'Foo'
}
print(json.dumps(d))   # {"name": "Foo"}

d['date'] = datetime.datetime.now()
print(json.dumps(d))   # TypeError: datetime.datetime(2016, 4, 8, 11, 22, 3, 84913) is not JSON serializable
