CREATE TABLE person (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
);

INSERT INTO person (name) VALUES ('Joe');
INSERT INTO person (name) VALUES ('Jane');

SELECT * FROM person;


ALTER TABLE person ADD COLUMN phone TEXT;

SELECT * FROM person;

INSERT INTO person (name, phone) VALUES ('Marcus', '1234565');

SELECT * FROM person;

