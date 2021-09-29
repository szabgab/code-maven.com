from functools import partial

def full(number, name):
    print(f"{name} {number}")

names = ["foo"]
for name in names:
   exec(f'{name} = partial(full, name="{name.upper()}")')

foo(17)

