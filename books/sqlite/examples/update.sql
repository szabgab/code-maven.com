.mode batch

CREATE TABLE people (
    name TEXT,
    grade INTEGER
);

INSERT INTO people (name, grade) VALUES ('Joe', 40);
INSERT INTO people (name, grade) VALUES ('Jane', 60);
SELECT * from people;
SELECT '-------';

-- SELECT 'Setting the grade of Joe to be 44';
UPDATE people SET grade = 44;
SELECT * from people;
SELECT '-------';

UPDATE people SET grade = 100 WHERE name = 'Joe';
SELECT * from people;
SELECT '-------';

