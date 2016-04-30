import random

def main(x, y):
    z = helper(x)
    return y + z


def helper(q):
    if random.random() < 0.5:
        raise Exception("Bad luck")
    return q**2

