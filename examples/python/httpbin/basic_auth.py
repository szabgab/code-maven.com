import requests
# from requests.auth import HTTPBasicAuth

# auth=HTTPBasicAuth('foo', 'bar'))  #
res = requests.post('http://httpbin.org/basic-auth/foo/bar', auth=('foo', 'bar'))
print(res.status_code)
print(res.reason)
print()
for key, value in res.headers.items():
    print(f"{key} {value}")

print()
print(res.content)
# for key, value in res.json().items():
#     print(f"{key} {value}")
