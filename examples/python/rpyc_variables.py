import rpyc
import sys

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.classic.connect(server)
conn.execute('x = 21')
conn.execute('x *= 2')
print(conn.eval('x'))     # 42


conn.execute('scores = { "Foo" : 10 }')
conn.execute('scores["Foo"] += 1')
conn.execute('scores["Bar"] = 42')

local_scores = conn.eval('scores')
print(local_scores)         # {'Foo': 11, 'Bar': 42}
print(local_scores['Foo'])  # 11


conn.namespace["scores"]["Bar"] += 58
print(conn.eval('scores'))  # {'Foo': 11, 'Bar': 100}
