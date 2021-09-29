from functools import partial

def full(number, name):
    print(f"{name} {number}")


foo = partial(full, name='FOO')

foo(17)
