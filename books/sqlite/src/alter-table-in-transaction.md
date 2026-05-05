# ALTER TABLE in transaction

Even better, do all the changes inside a transaction. That way they are either all implemented, or nothing changes.


{% embed include file="examples/alter-table-in-transaction.sql" %}

```shell
$ sqlite examples/alter-table-in-transaction.sql
```

{% embed include file="examples/alter-table-in-transaction.out" %}
