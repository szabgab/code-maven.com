
a = "2"
b = "3"
puts a+b  # 23
puts '-------'

# puts "2"+3   # no implicit conversion of Fixnum into String (TypeError)

puts a.to_i # 2
puts a.to_f # 2.0
puts a.to_r # 2/1
puts a.to_c # 2+0i
puts '-------'

puts "11".to_i            # 11
puts "11".to_i(base=2)    # 3
puts "11".to_i(base=8)    # 9
puts "11".to_i(base=16)   # 17
puts '-------'

puts "aB".to_i(base=16)   # 171
puts "aB".to_i            # 0
puts "9".to_i(base=8)     # 0
puts '-------'

puts "2x3".to_i           # 2
puts "2 3".to_i           # 2
puts '-------'

c = "14.6"
puts c.to_i    # 14
puts c.to_f    # 14.6
puts c.to_r    # 73/5
puts c.to_c    # 14.6+0i
puts '-------'


e = "2.3e4x5"
puts e         # 2.3e4x5
puts e.to_i    # 2
puts e.to_f    # 23000.0
puts e.to_r    # 23000/1
puts e.to_c    # 23000.0+0i
puts '-------'


