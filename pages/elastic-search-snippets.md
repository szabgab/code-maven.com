---
title: "Elastic Search - updating complex data structure"
timestamp: 2019-06-25T06:30:01
tags:
  - ElasticSearch
published: true
author: szabgab
archive: true
---


Just some snippets for experimenting with ElasticSearch


```
GET _search
{
  "query": {
    "match_all": {}
  }
}
```

```
POST /exp/experiments/
{
    "name" :"Blue experiment",
    "state": "running",
    "message": [
      {
        "txt" : "start",
        "ts": "2018-01-01T07:30:01",
        "status" : "received"
      }
    ]
}
```

```
POST /exp/experiments/
{
    "name" : "Green experiment",
    "state": "running",
    "message": [
      {
        "txt" : "start",
        "ts": "2018-01-02T07:30:01",
        "status" : "received"
      }
    ]
}
```

```
GET /exp/experiments/_search
```

```
# PUT /exp/experiments/1234
# same as POST but specifies the _id of the document

# POST and PUT both "index" a document
# DELETE /exp   deleting the whole index
```

```
POST /exp/experiments/_bulk
{ "index" : { "_id" : 1 }}
{...}
{ "index" : { "_id" : 2 }}
{...}
```


```
GET /exp/experiments/_search
{
  "query": {
    "match": {
      "name": "experiment"
    }
  }
}
# match looking for single word
# match_phrase looking for the phrase (multiple words) in that order
```

```
PUT /test/_doc/1
{
  "counter": 0,
  "name" : "Foo",
  "tags" : ["apple", "banana"]
}
```

```
POST /test/_doc/1/_update
{
    "script" : {
        "source": "ctx._source.counter += params.count",
        "lang": "painless",
        "params" : {
            "count" : 4
        }
    }
}
```

```
POST /test/_doc/1/_update
{
    "script" : {
        "source": "ctx._source.tags.add(params.tag)",
        "lang": "painless",
        "params" : {
            "tag" : "peach"
        }
    }
}
```

```
DELETE /test
GET /test/_doc/_search
GET /test/_mapping/_doc
```

```
POST /test/_doc/1/_update
{
    "script" : "ctx._source.new_field = 'value_of_new_field'"
}
POST /test/_doc/1/_update
{
    "script" : "ctx._source.remove('ppl')"
}
POST /test/_doc/1/_update
{
    "script" : "ctx._source.tags._index.0 = 'xxx'"
}
```

```
POST /test/_doc/1/_update
{
    "script" : "ctx._source.ppl = params.people",
    "params" : {
      "people" : "xxx"
    }
}
```

```
POST /test/_update_by_query
{
  "script": {
    "source": "ctx._source.counter++",
    "lang": "painless"
  },
  "query": {
    "term": {
      "_id": 1
    }
  }
}
```

```
PUT /test/_doc/2
{
  "counter": 0,
  "name" : "Foo",
  "internal" : {
    "counter" : 0
  },
  "tags" : ["apple", "banana"],
  "ppl"  : [
     {"name": "Foo", "age" : 23},
     { "name" : "Bar", "age" : 19}
  ]
}
```

```
POST /test/_update_by_query
{
  "script": {
    "source": "ctx._source.internal.counter++",
    "lang": "painless"
  },
  "query": {
    "term": {
      "_id": 2
    }
  }
}
```

```
POST /test/_update_by_query
{
  "script": {
    "source": "ctx._source.ppl.0.age++",
    "lang": "painless"
  },
  "query": {
    "term": {
      "_id": 2
    }
  }
}
```

```
GET /test/_doc/_search
POST /test/_update_by_query
{
  "script": {
    "source": "ctx._source.ppl.add(params.person)",
    "lang": "painless",
    "params": {
      "person": {
        "name" : "Zorg",
        "age" : 100
      }
    }
  },
  "query": {
    "term": {
      "_id": 2
    }
  }
}

POST /test/_update_by_query
{
  "script": {
    "source": "ctx._source.ppl.remove(0)",
    "lang": "painless"
  },
  "query": {
    "term": {
      "_id": 2
    }
  }
}

POST /test/_update_by_query
{
  "script": {
    "source": "ctx._source.ppl.0.address = 'Middle Earth'",
    "lang": "painless"
  },
  "query": {
    "term": {
      "_id": 2
    }
  }
}

```
