
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
    import sys
    if len(sys.argv) < 1:
        exit("Usage: {} FILENAMEs".format(sys.argv[0]))
    results = wc(*sys.argv[1:])
    for filename in results:
        res = results[filename]
        print("{} {} {} {}".format(res['lines'], res['words'], res['chars'], filename))


# from wc import wc
def test_wc(tmpdir):
    import os

    assert wc() == {}

    temp_dir = str(tmpdir)
    print(temp_dir)

    filename = os.path.join(temp_dir, 'a.txt')
    with open(filename, 'w') as fh:
        fh.write("Hello World\n")
        fh.write("Second line\n")

    assert wc(filename) == {
        filename : {
            'lines': 2,
            'words': 4,
            'chars': 24,
        }
    }
