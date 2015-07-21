#!/usr/bin/env python
from __future__ import print_function

class Fibonacci(object):
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.values = []

    def __iter__(self):
        return self

    def next(self):
        self.count += 1
        if self.count > self.limit:
            raise StopIteration

        if len(self.values) < 2:
            self.values.append(1)
        else:
            self.values = [self.values[-1], self.values[-1] + self.values[-2]]
        return self.values[-1]


for f in Fibonacci(5):
    print(f)
    if f % 17 == 0:
        print('found')
        break

print('-----')

for f in Fibonacci(15):
    print(f)
    if f % 17 == 0:
        print('found')
        break
