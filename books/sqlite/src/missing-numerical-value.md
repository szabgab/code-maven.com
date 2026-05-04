# Missing numerical value

{% embed include file="examples/missing-integer-value.sql" %}

```shell
$ sqlite3 < examples/missing-integer-value.sql
2+2|4
2-2|0
Meaning of life?|
```

```
╭──────────────────┬────────╮
│     question     │ answer │
╞══════════════════╪════════╡
│ 2+2              │      4 │
│ 2-2              │      0 │
│ Meaning of life? │ NULL   │
╰──────────────────┴────────╯
```

