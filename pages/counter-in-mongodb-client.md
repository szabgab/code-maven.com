---
title: "Counter in MongoDB client"
timestamp: 2015-09-25T10:30:01
tags:
  - MongoDB
  - insert
  - find
  - update
  - _id
  - $inc
  - findAndModify
  - upsert
published: true
books:
  - mongodb
author: szabgab
archive: true
---


In the [big counter example](/counter) mostly we use programming languages, but this time I am going to use the MongoDB client
to implement a counter. Later we can use this example to build counters using some programming language and MongoDB as the storage facility.


Launch the MongoDB client and connect to MongoDB server:

```
$ mongo
```

Switch to a database: (We call it `test`)

```
> use test
```


List the existing collections (there are none):

```
> show collections
system.indexes  0.000MB / 0.000MB
```


Alternatively, list all the entries in the `counter` collection: (there are none):

```
> db.counter.find()
Fetched 0 record(s) in 0ms
```

## Insert a counter

Insert a document where we decide the `_id`, this is going to be the key of the counter,
and it has aanother field called 'val' that is set to the initial value of 1.


```
> db.counter.insert({ '_id' : 'a', 'val' : 1 })
Inserted 1 record(s) in 9ms
WriteResult({
  "nInserted": 1
})
```

## Retreive a document

We can retreive the counter by specifying its name:

```
> db.counter.find( { '_id' : 'a' })
{
  "_id": "a",
  "val": 1
}
Fetched 1 record(s) in 1ms
```


## Increment the counter

```
> db.counter.update({ '_id' : 'a'}, {'$inc' : { 'val' : 1 } })
Updated 1 existing record(s) in 3ms
WriteResult({
  "nMatched": 1,
  "nUpserted": 0,
  "nModified": 1
})
```

and retreive the new value:

```
> db.counter.find( { '_id' : 'a' })
{
  "_id": "a",
  "val": 2
}
```


## Insert another counter

```
> db.counter.insert({ '_id' : 'b', 'val' : 1 })
```

Increment both of them separately:

```
> db.counter.update({ '_id' : 'a'}, {'$inc' : { 'val' : 1 } })
> db.counter.update({ '_id' : 'a'}, {'$inc' : { 'val' : 1 } })
> db.counter.update({ '_id' : 'a'}, {'$inc' : { 'val' : 1 } })
> db.counter.update({ '_id' : 'b'}, {'$inc' : { 'val' : 1 } })
```


## Retreive the individual counters

```
> db.counter.find( { '_id' : 'a' })
{
  "_id": "a",
  "val": 5
}
Fetched 1 record(s) in 1ms
```

```
> db.counter.find( { '_id' : 'b' })
{
  "_id": "b",
  "val": 2
}
Fetched 1 record(s) in 0ms
```


## Retreive all the counters


```
> db.counter.find()
{
  "_id": "a",
  "val": 5
}
{
  "_id": "b",
  "val": 2
}
Fetched 2 record(s) in 1ms
```

## findAndModify and upsert

An even better solution is to use the `findAndModify` function call, and even include an
`upsert` field to make sure the docuemnt is created if it does not exist.

```
> db.counter.findAndModify({ query: { '_id' : 'y' }, update : { '$inc' : { val : 1 } }, new: true, upsert: true })
{
  "_id": "y",
  "val": 1
}
```





