import os

filename = 'count.txt'

def inc():
    if os.path.exists(filename):
        with open(filename) as fh:
            count = int(fh.read())
    else:
        count = 0

    count += 1
    with open(filename, 'w') as fh:
        fh.write(str(count))

    return count

for _ in range(10000):
    try:
        res = inc()
    except Exception:
        pass
print(res)
