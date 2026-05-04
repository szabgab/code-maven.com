# Field with DEFAULT value

We can set up a `DEFAULT` value to each field and if the `INSERT` does not set the value then this default value will be set.
However, if the `INSERT` explicitly sets `NULL` then that will be the value.

{% embed include file="examples/default-value.sql" %}

```
$ sqlite3 < examples/default-value.sql
```

{% embed include file="examples/default-value.out" %}

```
╭──────────────────┬────────╮
│     question     │ answer │
╞══════════════════╪════════╡
│ Language?        │ SQL    │
│ Database?        │ SQLite │
│ Meaning of life? │ '42'   │
│ What is void?    │ NULL   │
╰──────────────────┴────────╯
```
