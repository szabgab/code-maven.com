import sys

if len(sys.argv) < 2:
    exit("Usage: {} FILENAME".format(sys.argv[0]))

filename = sys.argv[1]

total1 = 0
with open(filename) as fh:
    for line in fh:
        total1 += int(line)
print(total1)


with open(filename) as fh:
    total2 = sum(map(int, fh.readlines()))
print(total2)
