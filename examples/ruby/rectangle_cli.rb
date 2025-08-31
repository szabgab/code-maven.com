if ARGV.size != 2
    puts "#{$PROGRAM_NAME} WIDTH LENGTH"
    exit 1
end

width = ARGV[0].to_f
length = ARGV[1].to_f

area = width * length
circumference = 2 * (width + length)
puts "area: #{area}"
puts "circumference: #{circumference}"
