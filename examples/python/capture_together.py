import subprocess
import sys
import os


def run(cmd):
    os.environ['PYTHONUNBUFFERED'] = "1"
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT,
    )
    stdout, stderr = proc.communicate()

    return proc.returncode, stdout, stderr

code, out, err = run([sys.executable, 'examples/python/run.py'])

print("out: '{}'".format(out))
print("err: '{}'".format(err))
print("exit: {}".format(code))


