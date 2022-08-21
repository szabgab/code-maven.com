import datetime
import time
import sys

param = ""

if len(sys.argv) > 1:
  param = sys.argv[1]

while True:
   with open("/tmp/timestamp.log", "a") as fh:
       fh.write(param + ' ' + str(datetime.datetime.now()) + "\n")
   time.sleep(1)

