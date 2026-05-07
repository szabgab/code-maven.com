# VARCHAR

You can define a column to be `VARCHAR(10)`, but SQLite will totally disregard it.
It can be still useful if your application code can rely on it or if at one point you
might want to migrate to another database respects such definitions.

You can't use this in a [STRICT](https://sqlite.org/stricttables.html) table.

{% embed include file="examples/varchar.sql" %}

```shell
$ sqlite3 < examples/varchar.sql
```

{% embed include file="examples/varchar.out" %}
