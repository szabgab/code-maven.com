import time
from random import random

from interval_timer import IntervalTimer

delta = 0.01
F = False
T = True

def run(sleeps):
    slp = 0
    intervals = []
    timestamps = []
    for interval in IntervalTimer(1):
        print(interval)
        timestamps.append(time.time())
        intervals.append(interval)
        sleep = sleeps[slp]
        slp += 1
        if slp >= len(sleeps):
            break
        time.sleep(sleep)
    # print(intervals)
    # print(len(sleeps))
    # print(len(intervals))
    return intervals, timestamps

def check_intervals_index(sleeps, intervals):
    for i in range(len(sleeps)):
        assert intervals[i].index == i

def run_test(sleeps, starts, misses):
    start = time.time()
    intervals, timestamps = run(sleeps)
    check_intervals_index(sleeps, intervals)

    for i in range(len(sleeps)-1):
        real_start = timestamps[i]-start
        print(real_start)
        assert starts[i]-delta < real_start, f"{i} {real_start} too small"
        assert real_start < starts[i]+delta, f"{i} {real_start} too big"
        assert intervals[i].missed is misses[i], f"{i} {sleeps[i]} missed?"

def test_basic():
    # start   0     1     2
    starts = [0,    1,    2]
    misses = [F,    F,    F]
    sleeps = [0.1,  0.1,  1]
    run_test(sleeps, starts, misses)

def test_missing():
    # start   0     1     2     3      4     5
    starts = [0,    1,    3.1,  3.6,   4,    5]
    misses = [F,    F,    T,    F,     F,    F]
    sleeps = [0.5,  2.1,  0.5,  0.1,   0.4,  0.5]
    run_test(sleeps, starts, misses)

def test_accumulated_missing():
    # start   0     1     2     3      4     5     6
    starts = [0,    1,    2.2,  3.5,   5.1,  5.6,  6]
    misses = [F,    F,    F,    F,     T,    F,    F]
    sleeps = [0.5,  1.2,  1.3,  1.6,   0.5,  0.2,  0.1]
    run_test(sleeps, starts, misses)


