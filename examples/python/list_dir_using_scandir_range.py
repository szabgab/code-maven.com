import os

path = "/home/gabor/work/code-maven.com/sites/en/pages/"

with os.scandir(path) as it:
    for _ in range(3):
        print(it.__next__().name)

