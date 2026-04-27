# Reject INSERT

The `INSERT` migh be rejected for various reasons. e.g. Incorrect type of data.
Here we try to insert a string `"tall"` for the `height` column while our table definition indicated that it is a `FLOAT`.

{% embed include file="src/examples/insert_people_bad.sql" %}

```
ERROR 1265 (01000): Data truncated for column 'height' at row 1
```

