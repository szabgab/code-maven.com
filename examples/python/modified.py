#!/usr/bin/env python

import sys
import os
import time
from datetime import datetime

now = time.time()
if len(sys.argv) < 2:
   exit(f"Usage: {sys.argv[0]} FILENAME")

filename = sys.argv[1]

mtime = os.path.getmtime( filename)
print(mtime)
print(now - mtime)


stat = os.stat( filename)
print(stat.st_mtime)
date = datetime.fromtimestamp(stat.st_mtime)
print(date)

# mtime = os.path.getmtime( os.path.join(log_dir, thing) )
# returns something else

