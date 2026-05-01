# CREATE - INSERT - SELECT

With `CREATE` we define the schema.

With `INSERT` we add a row.

With `SELECT` we can fetch data from the database.


{% embed include file="examples/create-insert-select.sql" %}

## In memory:

```shell
$ sqlite3 < create-insert-select.sql
```

{% embed include file="examples/create-insert-select.out" %}

## In file:

```shell
$ sqlite3 demo.db < create-insert-select.sql
```

{% embed include file="examples/create-insert-select.out" %}

Then, if we don't need it any more, we should remove the database file:


```
$ rm -f demo.db
```


