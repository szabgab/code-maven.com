
f = File.open($PROGRAM_NAME, 'r')
f.flock(File::LOCK_EX)
puts "Running #{$$}"
sleep 10
