#!/usr/bin/env python
from __future__ import print_function
import sys

r = range(10000)
x = xrange(10000)
print(type(r))    # <type 'list'>
print(type(x))    # <type 'xrange'>
