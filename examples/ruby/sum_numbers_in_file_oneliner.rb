
filename = '../data/numbers.txt'

puts "The total is #{open(filename).readlines.map(&:to_i).reduce :+}"

