# SQLite


Insert multiple values:

INSERT INTO tbl () VALUES (), (), ();


select date

Import Excel file
Export to CSV
Export to Excel


Check out the [SQL tutorial](https://www.sqltutorial.org/)

[SQLite tutorial](https://www.sqlitetutorial.net/)


* query optimization
* migrations - changes between schema version
* Show complex queries
* Show other tools.

FOREIGN KEY with multiple fields
INDEX with multiple fields
CONSTRAINT uid_pid UNIQUE (uid, pid)
VARCHAR(255)
UNIQUE

CREATE TRIGGER user_cleanup
  BEFORE DELETE ON user FOR EACH ROW
  BEGIN
   DELETE FROM subscription WHERE uid=OLD.id;
   DELETE FROM verification WHERE uid=OLD.id;
   DELETE FROM login_whitelist WHERE uid=OLD.id;
  END;

-----
Conditional CREATE

CREATE TABLE IF NOT EXISTS counters (
            name TEXT PRIMARY KEY,
            number INTEGER NOT NULL
        )


# Increment or Insert
INSERT INTO counters (name, number)
VALUES (?, 1)
ON CONFLICT(name) DO UPDATE SET number = number + 1",

