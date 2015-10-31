if ARGV.length < 1
    puts "Missing filename from the command line"
    exit;
end

count = []

filename = ARGV[0]
fh = open filename
fh.each do |line|
    chars = line.split('')
    chars.each do |c|
        if c != ' ' then
            if not count[c.to_i] then
                count[c.to_i] = 0
            end
            count[c.to_i] += 1
        end
    end
end

(0..9).each do |i|
    print i, '    ', ( count[i] ? count[i] : 0), "\n"
end


