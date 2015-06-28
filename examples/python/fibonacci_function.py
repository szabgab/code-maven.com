#!/usr/bin/env python
from __future__ import print_function

def fibonacci():
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]

if __name__ == '__main__':
    fibonacci()
