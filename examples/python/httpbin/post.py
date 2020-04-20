import requests

res = requests.post('http://httpbin.org/post', data={"name": "Foo Bar"})
print(res.status_code)
print(res.reason)
print()

print("Headers:")
for key, value in res.headers.items():
    print(f"{key} {value}")

print()
#print(res.content)
for key, value in res.json().items():
    if key == "headers":
        continue
    print(f"{key} {value}")
