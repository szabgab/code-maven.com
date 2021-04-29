import os
import time
import random

def child_process():
    sleep = random.randint(1, 5)
    exit_code  = random.randint(0, 2)
    print(f"In child {os.getpid()} waiting for {sleep} and then exiting with {exit_code}")
    time.sleep(sleep)
    exit(exit_code)

def main():
    count = 3
    processes = []

    for _ in range(count):
        pid = os.fork()
        if pid == 0:
            child_process()
        else:
           processes.append(pid)

    while processes:
        pid, exit_code = os.wait()
        #pid, exit_code = os.waitpid(-1, os.WNOHANG)
        if pid == 0:
            print("do something else or just wait 1 sec")
            time.sleep(1)
        else:
            print(pid, exit_code//256)
            processes.remove(pid)

main()
