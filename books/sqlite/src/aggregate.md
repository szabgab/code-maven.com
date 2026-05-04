# Aggregate: COUNT, AVG, MAX, MIN

[Aggregare functions](https://sqlite.org/lang_aggfunc.html)

{% embed include file="examples/grades.sql" %}

{% embed include file="examples/aggregate.sql" %}

```shell
$ cat examples/grades.sql  examples/aggregate.sql | sqlite3
```

{% embed include file="examples/aggregate.out" %}
