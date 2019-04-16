import pylev
import timeit
import sys

def non_cached(a, b):
    return pylev.levenshtein(a, b)

def cached(a, b):
    if 'data' not in cached.__dict__:
        cached.data = {}
    k = (a,b)
    if k not in cached.data:
        cached.data[k] = pylev.levenshtein(a, b)
    return cached.data[k]

if len(sys.argv) != 2:
    exit("Need 1 argument, number of iterations")

n = int(sys.argv[1])
a = 'fsffvfdsbbdfvvdavavavavavava'
b = 'fvdaabavvvvvadvdvavavadfsfsdafvvav'


print(timeit.timeit(lambda : non_cached(a, b), number=n))
print(timeit.timeit(lambda : cached(a, b), number=n))

