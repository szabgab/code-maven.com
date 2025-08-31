---
title: "Getting started with SurrealDB using Python and Docker"
timestamp: 2024-02-24T12:30:01
tags:
  - SurrealDB
  - CREATE
  - UPDATE
  - SET
  - DELETE
description: "SurrealDB is a new multi-model database. We are using it from Python."
published: true
books:
  - python
  - surrealdb
author: szabgab
archive: true
show_related: true
---


[SurrealDB](https://surrealdb.com/) is a multi-model database I have been experimenting with in Rust. I created a number of examples for [SurrealDB using Rust](https://rust.code-maven.com/surrealdb).
In this article we take a look at the basics of SurrealDB using Python.


## Install SurrealDB - run it using Docker

You can fully install SurrealDB on your computer, but I prefer to run everything inside [Docker containers](/docker). That makes it easier to shut down processes when I don't need them
or even uninstall them if I stop using them or stop experimenting with them.

In this case I started SurrealDB as was recommended on the [Docker Hub](https://hub.docker.com/r/surrealdb/surrealdb) using an in-memory database.
One of the advantages of using in-memory database is that when I shut down the docker container all the data is also gone. This is often better when I experiment.

```
docker run --rm --pull always --name surrealdb -p 8000:8000 surrealdb/surrealdb:latest \
   start --log trace --user root --pass root memory
```

This will start  Docker container and SurrealDB will listen on port 8000.

## Install Python requirements

For this example I was using Python 3.11.6 on Ubuntu Linux.

Created a virtual environment and installed the surrealDB client:

{% include file="examples/python/surrealdb-getting-started/requirements.txt" %}

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Walking through the code

At the bottom of this page you will find the whole example, here I'll walk through the statements.


Import the required modules.

```python
from surrealdb import Surreal
import asyncio

```

We are going to use async here.
```python
async def main():
```

Connect to the server. Our Docker container runs on localhost and listens on port 8000.

```python
    async with Surreal("ws://localhost:8000/rpc") as db:
```

Signin. Authenticate with the server.

We created this user/password pair with the parameters we provided to the <b>docker run</b> command above.

In a real application you'd probably take the values of the user and the password from some external source.
```python
        await db.signin({"user": "root", "pass": "root"})
```

Select the "namespace" and the "database".
These provide a 2-level separation for your organization and project structure.
You can use any name here.

```python
        await db.use("test_namespace", "test_database")
```

Insert some data in the "character" table. There is no need to create the table up-front and there is no need to create a schema.
In this table we will have two columns: "name" and "race" with values.
As we are passing a Python data structure here we could have variables instead of the individual values or instead of the whole dictionary.

```python
        res = await db.create(
            "character",
            {
                "name": "Jake Sully",
                "race": "human",
            },
        )
        print(res)
```

This is the first time we look at the result returned by the method call. It is a list of the data entries we just added. Of course there is only one
entry in this list. SurrealDB automatically generated a unique ID for this record.

```
[{'id': 'character:xjoowpffazrmyhmxvne5', 'name': 'Jake Sully', 'race': 'human'}]
```

We add two more records in the exact same way.

```python
        res = await db.create(
            "character",
            {
                "name": "Miles Quaritch",
                "race": "human",
            },
        )
        print(res)

        res = await db.create(
            "character",
            {
                "name": "Neytiri",
                "race": "na'vi",
            },
        )
        print(res)
```

... and we get the results:

```
[{'id': 'character:hgaeik8egyzfderahyg2', 'name': 'Miles Quaritch', 'race': 'human'}]
[{'id': 'character:i132huv4isnl6nny0n80', 'name': 'Neytiri', 'race': "na'vi"}]
```


We can now get all the records from the "character" table using the <b>select</b> method.


```python
        res = await db.select("character")
        print(res)
```

Result: (I changed the layout to make it nicer in the post)

```
[
    {'id': 'character:hgaeik8egyzfderahyg2', 'name': 'Miles Quaritch', 'race': 'human'},
    {'id': 'character:i132huv4isnl6nny0n80', 'name': 'Neytiri', 'race': "na'vi"},
    {'id': 'character:xjoowpffazrmyhmxvne5', 'name': 'Jake Sully', 'race': 'human'}
]
```


Of course we might want to get only selected records or selected fields from those records.
We'll see that next, but first let's see that we can use the <b>query</b> method to get all the data from the "character" table.

```python
        res = await db.query("SELECT * FROM character")
        print(res)
```

And the prettified result.
It is a bit different from what we got before, but the content is there.

```
[
    {
        'result':
            [
                {'id': 'character:hgaeik8egyzfderahyg2', 'name': 'Miles Quaritch', 'race': 'human'},
                {'id': 'character:i132huv4isnl6nny0n80', 'name': 'Neytiri', 'race': "na'vi"},
                {'id': 'character:xjoowpffazrmyhmxvne5', 'name': 'Jake Sully', 'race': 'human'}i
            ],
        'status': 'OK',
        'time': '27.021µs'
    }
]
```

Select some data based on a conditions using SurrealQl which is similar to SQL.
This is only acceptable if we have hard-coded values to pass as in this example.
If the values are in variable you should never create the SQL statement using string formatting as that could easily lead to an [SQL Injection attack](https://bobby-tables.com/).

```python
        res = await db.query("SELECT * FROM character WHERE race='human'")
        print(res)
```

The result is the list of all the humans:

```
[
    {
        'result':
            [
                {'id': 'character:hgaeik8egyzfderahyg2', 'name': 'Miles Quaritch', 'race': 'human'},
                {'id': 'character:xjoowpffazrmyhmxvne5', 'name': 'Jake Sully', 'race': 'human'}
            ],
        'status': 'OK',
        'time': '56.296µs'
    }
]
```

If we have the values we would like to use in the statement in variables, then we should always use placeholder.
Here "$race" is just an arbitrary place-holder to what we assign a value in the attached dictionary.
The value, or the whole dictionary could have been Python variables.

```python
        res = await db.query("SELECT * FROM character WHERE race=$race", {
            'race': "na'vi",
        })
        print(res)
```

Result

```
[
    {
        'result': [
            {'id': 'character:i132huv4isnl6nny0n80', 'name': 'Neytiri', 'race': "na'vi"}
        ],
        'status': 'OK',
        'time': '58.079µs'
    }
]
```


Replace all the content in a table
This will keep the IDs, but it will replace the content. In the full-example below I have this commented out.

```python
        res = await db.update("character", {
            "race": "na'vi",
        })
```
```
[
    {
        'result':
            [
                {'id': 'character:hgaeik8egyzfderahyg2', 'race': "na'vi"},
                {'id': 'character:xjoowpffazrmyhmxvne5', 'race': "na'vi"}
                {'id': 'character:i132huv4isnl6nny0n80', 'race': "na'vi"},
            ],
        'status': 'OK',
        'time': '56.296µs'
    }
]
```

If we would like to change one (or more) fields in some selected rows we can use a query for that.
Here we replace the "race" field of a character with a given "name".

```python
        res = await db.query("UPDATE character SET race=$race WHERE name=$name", {
            'race': "na'vi",
            'name': "Jake Sully"
        })
        print(res)
```
```
[
    {
        'result':
            [
                {'id': 'character:xjoowpffazrmyhmxvne5', 'name': 'Jake Sully', 'race': "na'vi"}
            ],
        'status': 'OK',
        'time': '77.526µs'
    }
]
```

Let's see what is now in the database:

```python
        res = await db.select("character")
        print(res)

/code>
```
[
    {'id': 'character:hgaeik8egyzfderahyg2', 'name': 'Miles Quaritch', 'race': 'human'},
    {'id': 'character:i132huv4isnl6nny0n80', 'name': 'Neytiri', 'race': "na'vi"},
    {'id': 'character:xjoowpffazrmyhmxvne5', 'name': 'Jake Sully', 'race': "na'vi"}
]
```

At the end of this demo session we remove all the entries from the "character" table using the <b>delete</b> method so if we run the program again it will start from an empty database.

```python
        res = await db.delete("character")
        print(res)
```

It returns all the data that was deleted:

```
[
    {'id': 'character:hgaeik8egyzfderahyg2', 'name': 'Miles Quaritch', 'race': 'human'},
    {'id': 'character:i132huv4isnl6nny0n80', 'name': 'Neytiri', 'race': "na'vi"},
    {'id': 'character:xjoowpffazrmyhmxvne5', 'name': 'Jake Sully', 'race': "na'vi"}
]
```


## The whole example

{% include file="examples/python/surrealdb-getting-started/app.py" %}


## Conclusion

I think this is enough for now, you can already start playing with SurrealDB using these examples.


