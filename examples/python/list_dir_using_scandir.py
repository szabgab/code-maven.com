import os

path = "/home/gabor/work/code-maven.com/sites/en/pages/"
count = 0

with os.scandir(path) as it:
    for entry in it:
        print(entry.name)
        count += 1
        if count > 3:
            exit()

