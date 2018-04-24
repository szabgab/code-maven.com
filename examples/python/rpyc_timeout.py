import rpyc
import sys

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))

server = sys.argv[1]


conn = rpyc.classic.connect(server)
#conn = rpyc.classic.factory.connect(server, 18812, rpyc.classic.SlaveService, config={ 'sync_request_timeout' : 1 }, ipv6 = False, keepalive = False)
my_code = '''
import time
def wait_a_bit(n):
    start = time.time()
    #for _ in range(n):
    #    time.sleep(1)
    time.sleep(n)
    end = time.time()
    return { "start" : start, "end" : end, "diff" : int(end - start) }
'''
conn.execute(my_code)

rf = conn.namespace['wait_a_bit']
print(rf(50))


