if ARGV.length < 1
   puts "Needs an argument for age"
   exit
end

age = ARGV[0].to_f

if 18 < age and age < 23
    puts "In the range"
end


if 18 < age && age < 23
    puts "In the range"
end

