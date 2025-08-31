---
title: "Elasticseach administrative and configuration commands"
timestamp: 2019-07-20T12:30:01
tags:
  - elasticsearch
published: true
author: szabgab
archive: true
---


Just some random `curl` command that help me with the administration and the configuration of an Elasticsearch
cluster.




List of cats:

```
http://localhost:9200/_cat/
```

List indices:

```
http://localhost:9200/_cat/indices?v
```


Health of the system (should contain the word green)
```
http://localhost:9200/_cat/health
```

```
http://localhost:9200/_all/_settings
```


The health of the cluster:

```
http://localhost:9200/_cluster/health
```

Cluster settings

```
curl http://localhost:9200/_cluster/settings
```

Delete index:

```
curl  -X DELETE http://localhost:9200/index-name
```

Set temporary (transient) the low disk watermark

```
curl -X PUT http://localhost:9200/_cluster/settings  -H "Content-Type: application/json"  -d '{ "transient": {"cluster.routing.allocation.disk.watermark.low": "5%" } }'
```


Set the number of replicas to 1

```
curl -X PUT http://localhost:9200/experimental/_settings  -H "Content-Type: application/json"  -d '{ "index": {"number_of_replicas" : 1} }'
```

Tell the index to have no replicas. That is to have exactly one copy of each piece of data. No redundancy.
Useful if you only have a single node in your "cluster".

```
curl -X PUT http://localhost:9200/experimental/_settings  -H "Content-Type: application/json"  -d '{ "index": {"number_of_replicas" : 0} }'
```


