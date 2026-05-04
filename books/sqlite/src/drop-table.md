# DROP TABLE

`DROP TABLE` will remove the table and all its content. In this example we also used the `.schema` command to show what is the current schema
and the `.mode batch` to make the `SELECT` statement show a simple line.

{% embed include file="examples/drop-table.sql" %}

```shell
$ sqlite < examples/drop-table.sql
```

{% embed include file="examples/drop-table.out" %}
