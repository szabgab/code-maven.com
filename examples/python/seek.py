import os

filename = '/tmp/data.txt'
with open(filename, 'w') as fh:
    fh.write("Hello World!\nHow are you today?\nThank you!")

print(os.path.getsize(filename))  # 42

with open(filename) as fh:
    print(fh.tell())        # 0
    row = fh.readline()
    print(row)              # Hello World!
    print(fh.tell())        # 13

    fh.seek(-7, os.SEEK_CUR)
    print(fh.tell())        # 6

    row = fh.readline()
    print(row)              # World!
    print(fh.tell())        # 13

    fh.seek(0, os.SEEK_SET)
    print(fh.tell())        # 0
    print(fh.read(5))       # Hello

    fh.seek(-4, os.SEEK_END)
    print(fh.tell())        # 38
    print(fh.read())        # you!
    print(fh.tell())        # 42
