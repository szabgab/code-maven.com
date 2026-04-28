# SELECT date and time

[Date And Time Functions](https://sqlite.org/lang_datefunc.html)

{% embed include file="examples/date-and-time.sql" %}

```shell
$ sqlite3 < date-and-time.sql

date|2026-04-28
time|09:40:04
datetime|2026-04-28 09:40:04
julianday|2461158.90283096
unixepoch|1777369204
strftime|
strftime with param|2026-04-28 09:40:04
```
