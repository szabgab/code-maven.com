.mode batch
.import --csv examples/iris.csv iris


SELECT COUNT(*) FROM iris;

SELECT COUNT(*) FROM iris WHERE Species == 'Iris-virginica';
