import rpyc
import sys

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.classic.connect(server)
conn.execute('x = 42')
conn.execute('y = 0')
conn.execute('z = x/y')

print("Hello")

