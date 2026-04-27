# Import iris.csv


```
$ sqlite3

sqlite> .import --csv  -v iris.csv iris
CREATE TABLE "main"."iris"(
"Id" TEXT, "SepalLengthCm" TEXT, "SepalWidthCm" TEXT, "PetalLengthCm" TEXT,
 "PetalWidthCm" TEXT, "Species" TEXT)

Added 150 rows with 0 errors using 151 lines of input
```


```
sqlite> .schema
CREATE TABLE IF NOT EXISTS "iris"(
"Id" TEXT, "SepalLengthCm" TEXT, "SepalWidthCm" TEXT, "PetalLengthCm" TEXT,
 "PetalWidthCm" TEXT, "Species" TEXT);
```

```
sqlite> SELECT COUNT(*) FROM iris;
150

sqlite> SELECT AVG(SepalLengthCm) FROM iris;
5.84333333333333

sqlite> SELECT AVG(PetalLengthCm) FROM iris;
3.75866666666667

sqlite> SELECT AVG(PetalLengthCm), Species FROM iris GROUP BY Species;
1.464|Iris-setosa
4.26|Iris-versicolor
5.552|Iris-virginica
```

```
sqlite> DROP TABLE iris;
```


