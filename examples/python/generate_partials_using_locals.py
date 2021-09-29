from functools import partial

def full(number, name):
    print(f"{name} {number}")

locals()["foo"] = partial(full, name='Foo')

foo(17)

