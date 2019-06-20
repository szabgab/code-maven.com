iimport subprocess

def qxx(cmd):
    proc = subprocess.Popen(cmd,
               stdout = subprocess.PIPE,
               stderr = subprocess.STDOUT,
               shell = True,
    )
    stdout, stderr = proc.communicate()
    return stdout

