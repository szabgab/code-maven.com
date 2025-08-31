
if ARGV.length != 1
    puts "Usage: Needs filename"
    exit
end

fh = open ARGV[0]
fh.each do |line|
    if /REGEX/.match(line)
        print line
    end
end
