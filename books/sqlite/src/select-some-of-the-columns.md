# SELECT only some of the columns

Instead of using a `*` to fetch all the columns, we can define the specific columns we would like to fetch.

{% embed include file="examples/select-some-columns.sql" %}

```shell
$ sqlite3 < examples/select-some-columns.sql
```

{% embed include file="examples/select-some-columns.out" %}

