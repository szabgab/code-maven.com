import sys
import re

exp, filename = sys.argv[1:]

with open(filename) as fh:
   for line in fh:
       if exp in line:
           print(exp)
       #if re.search(exp, line):
       #    print(exp)

