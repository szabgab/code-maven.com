
filename = '../data/numbers.txt'

sum = 0
fh = open filename
fh.each do |line|
   sum += line.to_i
end
fh.close

puts "The total is #{sum}"

