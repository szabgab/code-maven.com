import os

path = "/home/gabor/work/code-maven.com/sites/en/pages/"
count = 0

for dirname, dirs, files in os.walk(path):
    for filename in files:
        print(os.path.join(dirname, filename))
        count += 1
        if count > 3:
            exit()

