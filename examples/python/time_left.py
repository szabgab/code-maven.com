import time
import datetime

class Timer(object):
    def __init__(self, total):
        self.start = datetime.datetime.now()
        self.total = total

    def remains(self, done):
        now  = datetime.datetime.now()
        #print(now-start)  # elapsed time
        left = (self.total - done) * (now - self.start) / done
        sec = int(left.total_seconds())
        if sec < 60:
           return "{} seconds".format(sec)
        else:
           return "{} minutes".format(int(sec / 60))


# There are 12987 units in this task
t = Timer(12987)

# do some work

time.sleep(1)
# after some time passed, or after some units were processed
# eg.  37 units, calculate, and print the remaining time:

print(t.remains(37))

# let the process continue and once in a while print the remining time.
