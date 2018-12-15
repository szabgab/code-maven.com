import consul

con = consul.Consul()
print(dir(con))
print(dir(con.catalog))
id, services = con.catalog.services()
print(id)

print('--- services ---')
for s in services:
   print(s)

print('---- service elastic --')
id, nodes = con.catalog.service('elastic')
print(id)

hosts = []
for n in nodes:
   print(n)
   hosts.append(n['Address'])
print(hosts)
