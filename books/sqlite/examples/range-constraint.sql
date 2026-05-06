CREATE TABLE grades (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE,
    value INTEGER,
    CHECK (value IS NULL OR (value BETWEEN 0 AND 100))
);

INSERT INTO grades (name, value) VALUES ('Joe', 100);
INSERT INTO grades (name, value) VALUES ('Jane', 200);
INSERT INTO grades (name, value) VALUES ('Mary', NULL);
INSERT INTO grades (name) VALUES ('Peter');
INSERT INTO grades (name, value) VALUES ('Zorg', 'hello');

SELECT * FROM grades;
