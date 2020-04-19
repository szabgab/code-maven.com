import requests

res = requests.get('http://httpbin.org/get?name=Foo')
print(res.status_code)
print(res.reason)
print()
for key, value in res.headers.items():
    print(f"{key} {value}")

print()
print(res.content)
for key, value in res.json().items():
    print(f"{key} {value}")
