import sys
import random

if len(sys.argv) != 4:
    exit(f"{sys.argv[0]} FILENAME NUMBER-OF-ROWS LENGTH-OF-ROWS")

_, filename, rows, length = sys.argv

line = "x" * int(length) + "\n"

match = random.randint(0, int(length))

with open(filename, 'w') as fh:
    for i in range(int(rows)):
        if i == match:
            fh.write("x" * (int(length)-2) + "yx\n")
        else:
            fh.write(line)
