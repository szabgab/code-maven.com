require "CSV"

filename = 'data.csv'
sum = 0
CSV.foreach(filename) do |row|
  sum += row[2].to_i
end

puts sum

