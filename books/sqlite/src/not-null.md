# NOT NULL constraint

{% embed include file="examples/not-null.sql" %}

```shell
$ sqlite3 < not-null.sql
1|Joe
|Jane
Runtime error near line 17: NOT NULL constraint failed: restricted.id (19)
1|Joe
```
