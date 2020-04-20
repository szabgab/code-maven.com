import requests

res = requests.get('http://httpbin.org/basic-auth/foo/bar', auth=('foo', 'hello'))
print(res.status_code)
print(res.reason)
print()
for key, value in res.headers.items():
    print(f"{key} {value}")
