import statsd 
import random
import time

c = statsd.StatsClient('localhost', 8125)

for _ in range(10):
    time.sleep(random.random() * 2)
    elapsed_time = random.random() * 3
    c.incr('demo.page_views')
    c.gauge('demo.elapsed_time', elapsed_time)

