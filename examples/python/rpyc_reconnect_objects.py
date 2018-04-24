import sys
import time
from rpyc_with_reconnect import ReConn

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))

conn = ReConn(sys.argv[1])

conn.execute('x = 21')
print(conn.eval('x'))     # 21
print("You have 10 sec to restart the RPyC server")
time.sleep(10)

conn.execute('y = 42')
print(conn.eval('y'))     # 42

print("You have 10 sec to restart the RPyC server")
time.sleep(10)
print(conn.eval('6*7'))     # 42


#conn.execute('x = 21')
#print(conn.eval('x'))     # 42
#print("assigned")
#time.sleep(80)
#print("waiting a bit more")
##time.sleep(20)
#conn.reconnect()
#conn.execute('x *= 2')
#print(conn.eval('x'))     # 42


