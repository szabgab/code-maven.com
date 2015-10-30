
if ARGV.length != 1 then
    puts "We need the name of the log file"
    exit
end

filename = ARGV[0]

count = {}

fh = open filename
fh.each do |line|
    length = line.index(' ')
    ip = line[0, length]
    if count[ip]
       count[ip] += 1
    else
       count[ip] = 1
    end
end

count.each do |k, v|
    puts "#{k}    #{v}"
end
