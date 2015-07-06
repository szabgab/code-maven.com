from __future__ import print_function
import urllib, sys


def fetch():
    if len(sys.argv) != 2:
        print("Usage: {} URL".format(sys.argv[0]))
        return
    url = sys.argv[1]
    f = urllib.urlopen(url)
    html = f.read()
    print(html)

fetch()
