from __future__ import print_function
import os
import subprocess
import sys

def run(cmd):
    os.environ['PYTHONUNBUFFERED'] = "1"
    proc = subprocess.Popen(cmd,
                            stdout = subprocess.PIPE,
                            stderr = subprocess.PIPE,
                            universal_newlines = True,
                            )
    stdout = []
    stderr = []
    mix = []
    while proc.poll() is None:
        line = proc.stdout.readline()
        if line != "":
            stdout.append(line)
            mix.append(line)
            print(line, end='')

        line = proc.stderr.readline()
        if line != "":
            stderr.append(line)
            mix.append(line)
            print(line, end='')

    return proc.returncode, stdout, stderr, mix

code, out, err, mix = run([sys.executable, 'examples/python/run.py'])

print("out: '{}'".format(out))
print("err: '{}'".format(err))
print("err: '{}'".format(mix))
print("exit: {}".format(code))

