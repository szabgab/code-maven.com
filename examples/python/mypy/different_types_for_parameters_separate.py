from typing import List

def handle_something(value: str) -> List[str]:
    return handle_many_things([value])

def handle_many_things(values: List[str]) -> List[str]:
    return values

print(handle_something("hello"))
print(handle_many_things(["hi", "there"]))
