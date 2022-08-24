import random
from typing import Optional

def get_something() -> Optional[float]:
    rnd = random.random()
    if rnd < 0.5:
        return rnd
    return None

print(get_something())
