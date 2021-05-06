import signal
import time

def handler(signum, frame):
    res = input("Ctrl-c was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)

signal.signal(signal.SIGINT, handler)

count = 0
while True:
    print(count)
    count += 1
    time.sleep(0.1)

