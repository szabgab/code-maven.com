import os
import sys
import filecmp
import difflib
import shutil

import pytest


root = os.path.dirname(__file__)
examples = os.listdir(os.path.join(root, 'examples'))

def check_diffs(dcmp):
    print(f'check_diffs {dcmp.left} and {dcmp.right}')
    assert dcmp.left_only == []
    assert dcmp.right_only == []
    success = True
    for filename in dcmp.diff_files:
        success = False
        print(f"File with difference: {filename}")
        with open(os.path.join(dcmp.left, filename)) as fh:
            left_content = fh.readlines()
        with open(os.path.join(dcmp.right, filename)) as fh:
            right_content = fh.readlines()
        for row in difflib.unified_diff(left_content, right_content):
            print(row, end="")
        print()

    #assert dcmp.diff_files == []
    for sub_dcmp in dcmp.subdirs.values():
        success = check_diffs(sub_dcmp) and success
    return success

@pytest.mark.parametrize("example", examples)
def test_examples(example, tmpdir, request):
    print(example)
    os.environ["PYTHONPATH"] = os.path.join(root, 'src')
    outdir = os.path.join(tmpdir, 'out')
    cmd = f"{sys.executable} -m sssimp --input {os.path.join(root, 'examples', example, 'input')} {outdir}"
    print(cmd)
    exit_code = os.system(cmd)
    assert exit_code == 0
    expected_output = os.path.join(root, 'examples', example, 'output')
    save = request.config.getoption("--save")
    if save:
        if os.path.exists(expected_output):
            shutil.rmtree(expected_output)
        shutil.move(outdir, expected_output)
        return

    dcmp = filecmp.dircmp(expected_output, outdir)
    print(expected_output, outdir)
    assert check_diffs(dcmp), "Some files differ. See above using the -s flag of pytest"

