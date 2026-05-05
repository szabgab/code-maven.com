# Multivalue fields

{% embed include file="examples/multivalue-fields.sql" %}

```shell
$ sqlite < examples/multivalue-fields.sql
```

{% embed include file="examples/multivalue-fields.out" %}

```
╭─────────┬────────────────────────────┬───────────╮
│ student │          subjects          │  grades   │
╞═════════╪════════════════════════════╪═══════════╡
│ Joe     │ Math,Chemistry,Programming │ 27,89,32  │
│ Jane    │ Math,Literature,Physics    │ 99,100,97 │
╰─────────┴────────────────────────────┴───────────╯
```
