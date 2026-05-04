# Invisible AUTOINCREMENT (ROWID)

If we have a column that is marked as `INTEGER PRIMARY KEY`, it will get incremented automatically. See the [AUTOINCREMENT](https://sqlite.org/autoinc.html) description for details.


{% embed include file="examples/invisible-autoincrement.sql" %}

```shell
$ sqlite3 < examples/invisible-autoincrement.sql
```

{% embed include file="examples/invisible-autoincrement.out" %}

