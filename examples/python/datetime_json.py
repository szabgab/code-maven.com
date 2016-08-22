import json
import datetime

d = {
   'name' : 'Foo'
}
print(json.dumps(d))   # {"name": "Foo"}

d['date'] = datetime.datetime.now()

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

print(json.dumps(d, default = myconverter))    # {"date": "2016-04-08 11:43:36.309721", "name": "Foo"}


