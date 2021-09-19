import sys
import re

if len(sys.argv) != 3:
    exit(f"{sys.argv[0]} FILENAME LIMIT")

_, filename, limit = sys.argv

def grep(regex, filename):
    with open(filename) as fh:
        for line in fh:
            if re.search(regex, line):
                print(line, end='')

i = int(limit)

while i:
    i-=1
    grep('y', filename)
