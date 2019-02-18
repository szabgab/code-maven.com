
##if __name__ == '__main__':
#def load():
#import sys
#print(sys.path)
#me = sys.path.pop(0)
#print(me)
#sys.path.append('/usr/lib/python2.7')
#print(sys.path)
#import random as rnd

import imp
print('xxx')
#rnd = imp.load_source('rnd', '/usr/lib/python2.7/random.py')
rnd = imp.load_source('rnd', '/usr/lib/python3.6/random.py')

first = True

def random():
    global first
    if first:
        rnd.seed(42)
        first = False
    return rnd.random()
