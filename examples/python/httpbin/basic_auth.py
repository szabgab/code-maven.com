import requests

# curl -i --user foo:bar https://httpbin.org/basic-auth/foo/bar

res = requests.get('http://httpbin.org/basic-auth/foo/bar', auth=('foo', 'bar'))
print(res.status_code)
print(res.reason)
print()
for key, value in res.headers.items():
    print(f"{key} {value}")

print()
print(res.content)
# for key, value in res.json().items():
#     print(f"{key} {value}")
