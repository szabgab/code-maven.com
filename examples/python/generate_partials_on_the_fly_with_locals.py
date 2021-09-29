from functools import partial

def full(number, name):
    print(f"{name} {number}")


names = ["foo"]

for name in names:
   locals()[name] = partial(full, name=name.upper())

foo(17)

