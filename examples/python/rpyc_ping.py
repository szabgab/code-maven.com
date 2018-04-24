import rpyc
import sys
import time

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.classic.connect(server)
rsys = conn.modules.sys
print(rsys.version)

for _ in range(10):
    print("pinging")
    conn.ping()
    #try:
    #    conn.ping()
    #except Exception as e:
    #    print(e)
    #    conn = rpyc.classic.connect(server)
    time.sleep(3)
    print("after wait")
    time.sleep(3)
    print("after more wait")

    # raise EOFError("connection closed by peer")

ros = conn.modules.os
print(ros.uname())
   # ConnectionRefusedError: [Errno 61] Connection refused 
