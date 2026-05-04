.mode batch
.import --csv  -v examples/iris.csv iris
SELECT '------';
.schema
SELECT '------';


SELECT COUNT(*) FROM iris;
SELECT AVG(SepalLengthCm) FROM iris;
SELECT AVG(PetalLengthCm) FROM iris;
SELECT AVG(PetalLengthCm), Species FROM iris GROUP BY Species;
