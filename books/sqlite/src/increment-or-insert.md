# Increment or Insert (UPSERT)

The [ON CONFLICT](https://sqlite.org/lang_conflict.html) clause is a non-standard extension specific to SQLite.

This way of using `ON CONFLICT` is also referred to as [UPSERT](https://sqlite.org/lang_upsert.html) (which is not a keyword in SQLite).

{% embed include file="examples/increment-or-insert.sql" %}

```shell
$ sqlite < examples/increment-or-insert.sql
```

{% embed include file="examples/increment-or-insert.out" %}

