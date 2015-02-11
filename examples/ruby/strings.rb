puts "Hello".length     # 5
puts "Hello".reverse    # olleH

puts "Jar " * 2         # Jar Jar
puts 2 * 3              # 6

puts "2".to_s * 3       # 222
puts 2.to_s * 3         # 222

puts 2 * "Jar " 
 #   examples/ruby_strings.rb:7:in `*': String can't be coerced into Fixnum (TypeError)
 #      from examples/ruby_strings.rb:7:in `<main>'
