rm -f /tmp/before.db /tmp/after.db
~/bin/sqlite3 /tmp/before.db < examples/before.sql
~/bin/sqlite3 /tmp/after.db < examples/after.sql
~/bin/sqldiff /tmp/before.db /tmp/after.db

