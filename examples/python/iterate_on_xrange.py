from __future__ import print_function
import sys

r = xrange(10000)

for v in r:
    pass

print(sys.getsizeof(r))  # 40
