import datetime
import time
import daemon

def main_program():
    while True:
        with open('/tmp/echo.txt', 'a') as fh:
            fh.write("{}\n".format(datetime.datetime.now()))
        time.sleep(1)

with daemon.DaemonContext():
    main_program()

