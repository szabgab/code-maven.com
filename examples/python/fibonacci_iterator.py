#!/usr/bin/env python
from __future__ import print_function

class Fibonacci(object):
    def __init__(self):
        self.values = []

    def __iter__(self):
        return self

    def next(self):
        if len(self.values) < 2:
            self.values.append(1)
        else:
            self.values = [self.values[-1], self.values[-1] + self.values[-2]]
        return self.values[-1]

for f in Fibonacci():
    if f % 17 == 0:
        print(f)
        break
    if f > 10000:
        break
