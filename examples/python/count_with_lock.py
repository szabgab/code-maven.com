import os
import fcntl

filename = 'count.txt'

def inc():
    if os.path.exists(filename):
        with open(filename, 'r+') as fh:
            fcntl.lockf(fh, fcntl.LOCK_EX)
            count = int(fh.read())
            count += 1
            fh.seek(0, os.SEEK_SET)
            fh.write(str(count))
    else:
        with open(filename, 'w') as fh:
            fcntl.lockf(fh, fcntl.LOCK_EX)
            count = 1
            fh.write(str(count))

    return count

for _ in range(10000):
    res = inc()
print(res)
