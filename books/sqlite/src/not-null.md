# NOT NULL constraint

Here we have two tables. In the `restricted` table we set one of the fields to be `NOT NULL`.

{% embed include file="examples/not-null.sql" %}

```shell
$ sqlite3 < examples/not-null.sql
```

{% embed include file="examples/not-null.out" %}
