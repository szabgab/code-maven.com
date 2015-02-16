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

print(team_a)    # {'Baz': 9, 'Foo': 3, 'Bar': 7}
print(team_b)    # {'Foo': 30, 'Moo': 10, 'Boo': 20}

team_a["b"] = team_b
print(team_a)    # {'Baz': 9, 'b': {'Foo': 30, 'Moo': 10, 'Boo': 20}, 'Foo': 3, 'Bar': 7}



team_b["Foo"] = 200
print(team_b)    # {'Foo': 200, 'Moo': 10, 'Boo': 20}
print(team_a)    # {'Baz': 9, 'b': {'Foo': 200, 'Moo': 10, 'Boo': 20}, 'Foo': 3, 'Bar': 7}
 
