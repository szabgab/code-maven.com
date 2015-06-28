#!/usr/bin/env python
from __future__ import print_function

def fibonacci():
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
        else:
            values = (values[-1], values[-1] + values[-2])
        yield values[-1]

for f in fibonacci():
    if f % 17 == 0:
        print(f)
        break
    if f > 10000:
        break
