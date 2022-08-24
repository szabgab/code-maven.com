import random

def get_something() -> float:
    rnd = random.random()
    if rnd < 0.5:
        return rnd
    return None

print(get_something())
