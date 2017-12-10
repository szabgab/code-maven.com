import numpy as np
from timeit import default_timer as timer
from numba import vectorize
import sys

if len(sys.argv) != 3:
    exit("Usage: " + sys.argv[0] + " [cuda|cpu] N(100000-11500000)")


@vectorize(["float32(float32, float32)"], target=sys.argv[1])
def VectorAdd(a, b):
    return a + b

def main():
    N = int(sys.argv[2])
    A = np.ones(N, dtype=np.float32)
    B = np.ones(N, dtype=np.float32)

    start = timer()
    C = VectorAdd(A, B)
    elapsed_time = timer() - start
    #print("C[:5] = " + str(C[:5]))
    #print("C[-5:] = " + str(C[-5:]))
    print("Time: {}".format(elapsed_time))

main()
