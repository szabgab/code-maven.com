# Missing value

When we insert data, some columns (besides the id) might be missing. SQLite will insert a [NULL](https://sqlite.org/nulls.html) value.

{% embed include file="examples/missing-text-value.sql" %}

```shell
$ sqlite3 < examples/missing-text-value.sql
Language?|SQL
Database?|SQLite
Meaning of life?|
```

This is hard to see in the above display, but in the interactive shell or if we use a real terminal it will look much better:

```
╭──────────────────┬────────╮
│     question     │ answer │
╞══════════════════╪════════╡
│ Language?        │ SQL    │
│ Database?        │ SQLite │
│ Meaning of life? │ NULL   │
╰──────────────────┴────────╯
```


