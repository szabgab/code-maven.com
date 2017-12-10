import numpy as np
from numba import vectorize
import math
from timeit import default_timer as timer

@vectorize(['float32(float32, int32)'], target='cpu')
def with_cpu(x, count):
    for _ in range(count):
        x = math.sin(x)
    return x

@vectorize(['float32(float32, int32)'], target='cuda')
def with_cuda(x, count):
    for _ in range(count):
        x = math.sin(x)
    return x

data = np.random.uniform(-3, 3, size=1000000).astype(np.float32)

for c in [1, 10, 100, 1000]:
    print(c)
    for f in [with_cpu, with_cuda]:
        start = timer()
        r = f(data, c)
        elapsed_time = timer() - start
        print("Time: {}".format(elapsed_time))

