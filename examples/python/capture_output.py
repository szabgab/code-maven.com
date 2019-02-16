import subprocess
import os
from contextlib import contextmanager
import tempfile
import shutil
import sys

@contextmanager
def tmpdir():
    dd = tempfile.mkdtemp()
    try:
        yield dd
    finally:
        shutil.rmtree(dd)

def run(cmd):
    with tmpdir() as dh:
       data = {
         'loc' : {},
         #'txt' : {},
         'file' : {},
         'write' : {},
         'read' : {},
       }
       channels = ['out', 'err']
       for ch in channels:
          data['loc'][ch] = 0
          #data['txt'][ch] = ''
          data['file'][ch] = dh + '/' + ch + '.txt'
          data['write'][ch] = open(data['file'][ch], 'w')
          data['read'][ch] = open(data['file'][ch], 'r')
       try:
           proc = subprocess.Popen(cmd,
               stdout=data['write']['out'],
               stderr=data['write']['err'],
               universal_newlines = True,
               )
           while proc.poll() is None:
               for ch in channels: 
                   size = os.path.getsize(data['file'][ch])
                   if size > data['loc'][ch]:
                       txt = data['read'][ch].read(size - data['loc'][ch])
                       print(txt, end='')
                       sys.stdout.flush()
                       data['loc'][ch] = size
       except Exception as e:
           print(e)

       for ch in channels: 
          data['write'][ch].close()
          data['read'][ch].close()

# open process to write to out.txt and err.txt, turn of buffering of stdout if possibl
# on every turn check the size of both files and read in as much as we can from each one of them

#run(['ls', '-l', '.', 'xxx', '..', 'yyy'])
run(['python', 'try.py'])
