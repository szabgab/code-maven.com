CREATE TABLE person (
    id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT
);

INSERT INTO person (name, email) VALUES ('Joe', 'joe@example.com');
INSERT INTO person (name, email) VALUES ('Jane', 'jane@example.com');
INSERT INTO person (name, email) VALUES ('Mary', 'mary@example.com');
INSERT INTO person (name, email) VALUES ('Peter', 'peter@example.com');

SELECT * from person;

.schema

