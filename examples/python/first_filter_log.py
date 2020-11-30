animals = ['snake', 'camel', 'etruscan shrew', 'ant', 'hippopotamus', 'giraffe']

def condition(animal):
    print(f"len({animal})")
    return len(animal) > 5

first = next(filter(condition, animals), None)
print(first)

