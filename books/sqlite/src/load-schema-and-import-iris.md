# Load schema and Import iris.csv

{% embed include file="examples/iris.sql" %}


```
sqlite> .schema
```


```
sqlite> .read iris.sql
```

```
sqlite> .import --csv --skip 1 -v iris.csv iris

Added 150 rows with 0 errors using 151 lines of input
```

```
sqlite> .schema
CREATE TABLE iris (
    Id            INTEGER,
    SepalLengthCm REAL,
    SepalWidthCm  REAL,
    PetalLengthCm REAL,
    PetalWidthCm  REAL,
    Species       TEXT
);
```


