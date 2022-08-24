import random
from typing import Union

def get_something() -> Union[float, None]:
    rnd = random.random()
    if rnd < 0.5:
        return rnd
    return None

print(get_something())
