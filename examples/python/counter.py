import os

counter_file = 'counter.txt'
if os.path.exists(counter_file):
    with open(counter_file) as fh:
        count = int(fh.read())
else:
    count = 0

count += 1
print(count)

with open(counter_file, 'w') as fh:
    fh.write(str(count))

