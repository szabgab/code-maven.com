import atexit
import sys


@atexit.register
def myexit():
    print("myexit")


if len(sys.argv) < 3:
    exit("Usage: {} A B".format(sys.argv[0]))

print(int(sys.argv[1]) / int(sys.argv[2]))

