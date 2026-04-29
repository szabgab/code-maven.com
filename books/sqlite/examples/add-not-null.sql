CREATE TABLE person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

INSERT INTO person (name) VALUES ('Joe');
INSERT INTO person (name) VALUES ('Jane');

SELECT * FROM person;

-- ALTER TABLE person ADD COLUMN phone TEXT NOT NULL;
-- Error near line 11: Cannot add a NOT NULL column with default value NULL

ALTER TABLE person ADD COLUMN phone TEXT;
UPDATE person SET phone = '123' WHERE name = 'Joe';
UPDATE person SET phone = '567' WHERE name = 'Jane';
SELECT * FROM person;

ALTER TABLE person ALTER phone SET NOT NULL;

-- INSERT INTO person (name) VALUES ('Mary');
-- Error near line 21: NOT NULL constraint failed: person.phone

INSERT INTO person (name, phone) VALUES ('Mary', '890');
SELECT * FROM person;

