#!/usr/bin/env python
from __future__ import division
import csv

file = '3-most-important-programming-languages.csv'

count = {}
total = 0
with open(file) as fh:
    rd = csv.reader(fh, delimiter=',')
    for row in rd:
        if row[0] == "Timestamp":
            continue
        for e in row[1:]:
            if e not in count:
                count[e] = 0
            count[e] += 1
            total += 1

s = 0
for k in sorted(count.keys(), key=lambda f: count[f], reverse=True):
    s += count[k]
    print("<tr><td>{}</td><td>{}</td><td>{} %</td></tr>".format(k, count[k], int(count[k]*10000/total)/100 ))

# verification
# print(total)
# print(s)
