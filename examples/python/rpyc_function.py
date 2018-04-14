import rpyc
import sys

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

filename = 'remote_code.py'

conn = rpyc.classic.connect(server)
with open(filename) as fh:
    my_code = fh.read()
    conn.execute(my_code)

rfib = conn.namespace['fib']
print(rfib(1))  # [1]
print(rfib(2))  # [1, 1]
print(rfib(5))  # [1, 1, 2, 3, 5]

