pair = [
   ('fname', 'Foo'),
   ('lname', 'Bar'),
   ('email', 'foo@bar.com'),
]

for p in pair:
    print('{} : {}'.format(p[0], p[1]))

for p in pair:
    print('{} : {}'.format(*p))

for field, value in pair:
    print('{} : {}'.format(field, value))
