import os
from contextlib import contextmanager
import tempfile
import shutil

@contextmanager
def cwd(path):
    '''
    # Usage:
    from mycontext import cwd
    with cwd(other_dir):
        # do something in the other_dir


    # Demo:
    from mycontext import cwd
    import os

    print(os.getcwd())
    with cwd('ansible'):
        print(os.getcwd())
    print(os.getcwd())
    '''

    oldpwd = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(oldpwd)

@contextmanager
def tmpdir():
    '''
    # Usage:
    from  import tmpdir
    with tmpdir() as dd:
        # store files in dd
        # the whole directory will be gone when the 'with' statement ends


    # Demo
    from mycontext import tmpdir
    import os

    with tmpdir() as d:
        print(d)
        os.system("touch " + d + "/abc")
        os.system("ls -l /tmp/")
        os.system("ls -l " + d)
    '''

    dd = tempfile.mkdtemp()
    try:
        yield dd
    finally:
        shutil.rmtree(dd)
