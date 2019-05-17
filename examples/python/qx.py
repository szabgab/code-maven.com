import subprocess

def qx(cmd):
   return subprocess.check_output(cmd, shell=True)

