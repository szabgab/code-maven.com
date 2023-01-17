import pathlib

path = pathlib.Path("/home/gabor/work/code-maven.com/sites/en/pages/")
count = 0

for thing in path.iterdir():
    count += 1
    print(thing)
    if count > 3:
        break
