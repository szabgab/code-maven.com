# SQLite

select date


Import Excel file
Export to CSV
Export to Excel


echo 'SELECT 2 + 3' | sqlite3



```
sqlite> .import --csv iris.csv iris
sqlite> SELECT COUNT(species) FROM iris;
150
sqlite> SELECT COUNT(DISTINCT species) FROM iris;
3
```

