import signal
import time
import readchar

def handler(signum, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True) # clear the printed line
        print("    ", end="\r", flush=True)


signal.signal(signal.SIGINT, handler)

count = 0
while True:
    print(f"{count}", end="\r", flush=True)
    count += 1
    time.sleep(0.1)

