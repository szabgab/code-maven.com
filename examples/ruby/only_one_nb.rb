
f = File.open($PROGRAM_NAME, 'r')
if (not f.flock(File::LOCK_EX | File::LOCK_NB))
    puts "Another instance is already running"
    exit
end
puts "Running #{$$}"
sleep 10
