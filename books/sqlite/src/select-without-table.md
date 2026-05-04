# SELECT without table

We can use `SELECT` event without tables to use SQLite as bloated calculator or to demonstrate some of the functions available.

{% embed include file="examples/add.sql" %}

```shell
$ sqlite3 < examples/add.sql
42
```

{% embed include file="examples/text.sql" %}

```shell
$ sqlite3 < examples/text.sql
Hello World
```
