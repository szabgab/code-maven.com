from __future__ import print_function

team_a = {
    'Foo' : 3,
    'Bar' : 7,
    'Baz' : 9,
}

 
team_b = {
    'Moo' : 10,
    'Boo' : 20,
    'Foo' : 30,
}

print(team_a)      # {'Baz': 9, 'Foo': 3, 'Bar': 7}
print(team_b)      # {'Foo': 30, 'Moo': 10, 'Boo': 20}

team = dict(team_a.items() + team_b.items())
print(team)        # {'Bar': 7, 'Foo': 30, 'Baz': 9, 'Boo': 20, 'Moo': 10}


team["Foo"] = 100
print(team)        # {'Bar': 7, 'Foo': 100, 'Baz': 9, 'Boo': 20, 'Moo': 10}
print(team_a)      # {'Baz': 9, 'Foo': 3, 'Bar': 7}
print(team_b)      # {'Foo': 30, 'Moo': 10, 'Boo': 20}


