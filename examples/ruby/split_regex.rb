require 'pp'

words_str = 'One   -  Two-  Three'
words_arr = words_str.split(/\s*-\s*/)   # ["One", "Two", "Three"]
pp words_arr

