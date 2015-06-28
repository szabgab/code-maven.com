#!/usr/bin/env python
from __future__ import print_function
import sys

l = [n*2 for n in range(1000)] # List comprehension
g = (n*2 for n in range(1000)) # Generator expression

print(type(l))  # <type 'list'>
print(type(g))  # <type 'generator'>

print(sys.getsizeof(l))  # 9032
print(sys.getsizeof(g))  # 80

print(l[4])   # 8
#print(g[4])   # TypeError: 'generator' object has no attribute '__getitem__'

for v in l:
    pass
for v in g:
    pass
