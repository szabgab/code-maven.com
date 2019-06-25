from datetime import datetime
from elasticsearch import Elasticsearch

hosts = ['localhost']
es = Elasticsearch(hosts)

index_name = 'experimental'

#res = es.search(index = index_name , body={"query": {"match_all": {}}})             # fetch all the records
#res = es.search(index = index_name , body={"query": {"match": {'name': 'Joe'} }})   # select by equality
#res = es.search(index = index_name , body={"query": {"match": {'name': 'Joe'} }}, size = 3)  # limit the number of results
#res = es.search(index = index_name , body={"query": {"range": {"rnd": {'gte': 20} }}})
#res = es.search(index = index_name , body={"query": {"range": {"timestamp": {'gte': datetime.now()} }}})  # some way to pass a datetime object
res = es.search(index = index_name , body={"query": {"range": {"timestamp": {'gte': '2019-03-13T12:02:49'} }}}) # or a string representing a date

print("Got {} Hits:".format(res['hits']['total']))
for hit in res['hits']['hits']:
    print(hit)

