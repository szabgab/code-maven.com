#!/usr/bin/env python
from __future__ import print_function
import os,sys

path = '.'

if len(sys.argv) == 2:
    path = sys.argv[1]


files = os.listdir(path)
for name in files:
    print(name)

