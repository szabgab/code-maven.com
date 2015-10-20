filename = '../data/numbers.txt'

fh = open(filename)
lines = fh.readlines
numbers = lines.map(&:to_i)
sum = numbers.reduce :+

puts "The total is #{sum}"


