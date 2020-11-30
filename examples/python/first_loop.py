animals = ['snake', 'camel', 'etruscan shrew', 'ant', 'hippopotamus', 'giraffe']

for animal in animals:
    if len(animal) > 5:
        first = animal
        break
else:
    first = None
print(first)   # etruscan shrew

