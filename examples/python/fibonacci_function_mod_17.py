#!/usr/bin/env python
from __future__ import print_function

def fibonacci():
    values = []
    while(True):
        if len(values) < 2:
            values.append(1)
        else:
            values = [values[-1], values[-1] + values[-2]]

        if values[-1] % 17 == 0:
            return(values[-1])

if __name__ == '__main__':
    res = fibonacci()
    print(res)
