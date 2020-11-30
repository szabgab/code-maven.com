animals = ['snake', 'camel', 'etruscan shrew', 'ant', 'hippopotamus', 'giraffe']

first = next(filter(lambda animal: len(animal) > 5, animals), None)
print(first)
print('-------')



filtered_list = filter(lambda animal: len(animal) > 5, animals)
print(filtered_list)
first = next(filtered_list, None)
print(first)
