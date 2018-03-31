require "csv"


filename = File.dirname(File.dirname(File.expand_path(__FILE__))) + '/data/distance.csv'
sum = 0
CSV.foreach(filename) do |row|
  sum += row[2].to_i
end

puts sum

