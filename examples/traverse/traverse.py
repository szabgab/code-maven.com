import os
import sys

root = '.'
if len(sys.argv) == 2:
    root = sys.argv[1]

for dirname, dirs, files in os.walk(root):
    pass
    for filename in files:
        print(os.path.join(dirname, filename))
