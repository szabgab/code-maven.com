import subprocess

def qxx(cmd):
    proc = subprocess.Popen(cmd,
               stdout = subprocess.PIPE,
               stderr = subprocess.STDOUT,
               shell = True,
    )
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        raise Exception("Error executing {}".formart(cmd))
    return stdout

