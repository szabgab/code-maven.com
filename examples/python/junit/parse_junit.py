import os
from junitparser import JUnitXml, Failure, Skipped, Error
import tempfile
import subprocess

def qxx(cmd):
    proc = subprocess.Popen(cmd,
               stdout = subprocess.PIPE,
               stderr = subprocess.PIPE,
               shell = True,
    )
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr

def main():
    tmpdir = tempfile.mkdtemp(prefix='test_reports')
    print(tmpdir)
    path = 'cases'
    cases = os.listdir(path)
    for case in cases:
        #print(case)
        if case != 'c.py':
            continue
        xml_file = os.path.join(tmpdir, f"{case}.xml")
        cmd_list = ['pytest', os.path.join(path, case), '--junitxml', xml_file]
        code, stdout, stderr = qxx(cmd_list)
        if code !=0:
            print(f"Execution failed with {code}")
            print(stdout)
            print(stderr)
            exit(1)
        with open(xml_file) as fh:
            print(fh.read())
            return
        xml = JUnitXml.fromfile(xml_file)
        for suite in xml:
            #print(suite)
            for case in suite:
                #print(type(case))
                print(case.name)
                if case.result:
                    print(case.result)
                    if isinstance(case.result, Failure):
                        print('  failure ', case.result.message)
                    if isinstance(case.result, Skipped):
                        print('  skipped ', case.result.message)

main()
