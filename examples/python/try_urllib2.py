from __future__ import print_function
import urllib2, sys


def fetch():
    if len(sys.argv) != 2:
        print("Usage: {} URL".format(sys.argv[0]))
        return
    url = sys.argv[1]
    try:
        f = urllib2.urlopen(url)
        html = f.read()
        print(html)
    except urllib2.HTTPError as e:
        print(e)

fetch()
