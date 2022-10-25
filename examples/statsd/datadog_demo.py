import datadog
import random
import time


for _ in range(10):
    time.sleep(random.random() * 2)
    elapsed_time = random.random() * 3
    datadog.statsd.increment('demo.page_views')
    datadog.statsd.gauge('demo.elapsed_time', elapsed_time)
    datadog.statsd.histogram('demo.elapsed_time_histogram', elapsed_time)

