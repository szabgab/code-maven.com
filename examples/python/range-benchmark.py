#!/usr/bin/env python
from __future__ import print_function
import timeit

r = range(10000)
x = xrange(10000)

def range_index():
    z = r[9999]

def range_xindex():
    z = x[9999]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("range_index()", setup="from __main__ import range_index",   number=10000000))
    print(timeit.timeit("range_xindex()", setup="from __main__ import range_xindex", number=10000000))
