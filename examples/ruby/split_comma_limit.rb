require 'pp'

words_str = 'Foo,Bar,Baz,Moo,Zorg'
words_arr = words_str.split(',', 3)
pp words_arr   # ["Foo", "Bar", "Baz,Moo,Zorg"]

