from elasticsearch import Elasticsearch
from datetime import datetime
import sys
import random
import time

def connect():
   es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
   return es

def list_indices(es):
    for index in es.indices.get('*'):
        print(index)
        print(index.__class__.__name__)
    print('---')

if __name__ == '__main__':
    es = connect()
    list_indices(es)

    for _ in range(100):
        es.index('experimental', doc_type = 'experimental', body = {
            'timestamp': datetime.utcnow(),
            'name': random.choice(['Doc', 'Grumpy', 'Happy', 'Sleepy', 'Bashful', 'Sneezy', 'Dopey', 'Snowwhite']),
            'load': random.random(),
        })
        time.sleep(1 + random.random())

