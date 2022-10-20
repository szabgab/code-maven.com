import sys

def wc(*filenames):
    results = {}
    for filename in filenames:
        chars = 0
        words = 0
        lines = 0
        try:
            with open(filename) as fh:
                for line in fh:
                    lines += 1
                    words += len(line.split())
                    chars += len(line)
            results[filename] = {
                'lines': lines,
                'words': words,
                'chars': chars,
            }
        except Exception as err:
            print(err)
    return results


if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit("Usage: {} FILENAMEs".format(sys.argv[0]))
    results = wc(*sys.argv[1:])
    totals = {
        'lines': 0,
        'words': 0,
        'chars': 0,
    }
    for filename in results:
        res = results[filename]
        print("{} {} {} {}".format(res['lines'], res['words'], res['chars'], filename))
        for k in res:
            totals[k] += res[k]
    print("{} {} {} {}".format(totals['lines'], totals['words'], totals['chars'], 'total'))


# from wc import wc
def test_wc(tmpdir):
    import os

    assert wc() == {}

    temp_dir = str(tmpdir)
    print(temp_dir)

    file_a = os.path.join(temp_dir, 'a.txt')
    with open(file_a, 'w') as fh:
        fh.write("Hello World\n")
        fh.write("Second line\n")

    file_b = os.path.join(temp_dir, 'b.txt')
    with open(file_b, 'w') as fh:
        fh.write("More than one    space\n")
        fh.write("Special - characters!\n")
        fh.write("No trailing newline")

    assert wc(file_a) == {
        file_a : {
            'lines': 2,
            'words': 4,
            'chars': 24,
        },
    }

    assert wc(file_b) == {
        file_b : {
            'lines': 3,
            'words': 10,
            'chars': 64,
        },
    }

    assert wc(file_a, file_b) == {
        file_a : {
            'lines': 2,
            'words': 4,
            'chars': 24,
        },
        file_b : {
            'lines': 3,
            'words': 10,
            'chars': 64,
        },
    }
