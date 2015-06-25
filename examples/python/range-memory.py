#!/usr/bin/env python
from __future__ import print_function
import sys

r = range(10000)
print(sys.getsizeof(r))  # 80072

x = xrange(10000)
print(sys.getsizeof(x))  # 40
