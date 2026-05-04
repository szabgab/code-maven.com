# STRICT Tables

If you really want, you can defined a table to be [STRICT](https://sqlite.org/stricttables.html),  but you need to do that on a per-table basis and the data types you can use are limited.

{% embed include file="examples/strict-table.sql" %}

```shell
$ sqlite < examples/strict-table.out
```

{% embed include file="examples/strict-table.out" %}


