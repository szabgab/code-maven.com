import os

filename = '/tmp/data.txt'

with open(filename, 'w') as fh:
   fh.write("Hello World!")

with open(filename) as fh:
   print(fh.read())

with open(filename, 'r+') as fh:
   print(fh.read())
   fh.seek(0, os.SEEK_SET)
   fh.write("Round")

with open(filename) as fh:
   print(fh.read())

