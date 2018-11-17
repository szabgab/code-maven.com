import subprocess
import sys


def run(cmd):
    proc = subprocess.Popen(cmd,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()

    return proc.returncode, stdout, stderr

code, out, err = run([sys.executable, 'examples/python/run.py'])

print("out: '{}'".format(out))
print("err: '{}'".format(err))
print("exit: {}".format(code))

