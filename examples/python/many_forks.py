import sys
import os

print("Process id before forking: {}".format(os.getpid()))

forks = 3
if len(sys.argv) == 2:
    forks = int(sys.argv[1])

for i in range(forks):
    try:
        pid = os.fork()
    except OSError:
        sys.stderr.write("Could not create a child process\n")
        continue

    if pid == 0:
        print("In the child process {} that has the PID {}".format(i+1, os.getpid()))
        exit()
    else:
        print("In the parent process after forking the child {}".format(pid))

print("In the parent process after forking {} children".format(forks))

for i in range(forks):
    finished = os.waitpid(0, 0)
    print(finished)

