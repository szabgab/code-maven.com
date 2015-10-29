
names = 'Foo', 'Bar', 'Baz'

puts names[0]   # Foo
puts names[1]   # Bar
puts names[2]   # Baz

puts names.length   # 3

puts names[3]       # (nothing)


puts names[-1]      # Baz

names[1] = 'Happy'
puts names[1]       # Happy


names[3] = 'Moo'
puts names[3]       # Moo
puts names.length   # 4

names[6] = 'Far Away'
puts names[6]       # Far Away
puts names.length   # 7
puts names[5]       # (nothing)

require 'pp'
pp names     # ["Foo", "Happy", "Baz", "Moo", nil, nil, "Far Away"]

names.push 'Hello', 'World'
pp names     # ["Foo", "Happy", "Baz", "Moo", nil, nil, "Far Away", "Hello", "World"]

last = names.pop
pp names    # ["Foo", "Happy", "Baz", "Moo", nil, nil, "Far Away", "Hello"]
puts last   # World
pp last     # "World"


last = names.pop 2
pp names    # ["Foo", "Happy", "Baz", "Moo", nil, nil]
pp last     # ["Far Away", "Hello"]


first = names.shift
pp names    # ["Happy", "Baz", "Moo", nil, nil]
puts first  # Foo


names.unshift 'Zorg', 'Morg'
pp names    # ["Zorg", "Morg", "Happy", "Baz", "Moo", nil, nil]

