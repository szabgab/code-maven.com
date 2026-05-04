# AUTOINCREMENT

Keeping in mind to increase the `id` number can be annoying. SQL provides the [AUTOINCREMENT](https://sqlite.org/autoinc.html) option
that can help us maintain that value. However in SQLite it is not necessary to use and it isn't even recommended.

In any case let's see an example:

{% embed include file="examples/autoincrement.sql" %}

```shell
$ sqlite3 < examples/autoincrement.sql
```

{% embed include file="examples/autoincrement.out" %}

