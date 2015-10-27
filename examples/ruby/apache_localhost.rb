
if ARGV.length != 1 then
    puts "We need the name of the log file"
    exit
end

filename = ARGV[0]

local = 0
remote = 0

fh = open filename
fh.each do |line|
    length = line.index(' ')
    ip = line[0, length]
    if ip == '127.0.0.1' then
        local = local+1
    else
        remote = remote+1
    end
end

puts "Number of remote requests is #{remote}. Number of local requests was #{local}"
