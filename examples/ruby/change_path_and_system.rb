system("echo $PATH")
ENV['PATH'] = '/nothing/here'
system("echo $PATH")
