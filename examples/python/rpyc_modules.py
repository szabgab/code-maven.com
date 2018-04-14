import rpyc
import sys

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]

conn = rpyc.classic.connect(server)
rsys = conn.modules.sys
print(rsys.version)

ros = conn.modules.os
print(ros.uname())
 
