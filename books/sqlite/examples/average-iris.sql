.mode batch
.import --csv examples/iris.csv iris


SELECT AVG(SepalLengthCm) FROM iris;
SELECT AVG(PetalLengthCm) FROM iris;
SELECT AVG(PetalLengthCm), Species FROM iris GROUP BY Species;
