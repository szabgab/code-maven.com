#!/usr/bin/env python

import requests
import time
import sys

url = 'http://10.2.11.5:5000/'

while True:
   #print(time.time())

   try:
       res = requests.get(url, timeout=0.3)
       if res.status_code == 200:
           print(res.content, end="")
       else:
           print("ERROR: {}".format(res.status_code))
   except Exception as e:
       print("EXCEPTION {}".format(e))
   sys.stdout.flush()
   time.sleep(1)

