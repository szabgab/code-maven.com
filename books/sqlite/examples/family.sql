PRAGMA foreign_keys = ON;

CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    father,
    mother
);
    --FOREIGN KEY(father) REFERENCES people(id)

INSERT INTO people (name) VALUES
    ('Abraham'),
    ('Hagar'),
    ('Sarah'),
    ('Keturah'),
    ('Ishmael'),
    ('Isaac'),
    ('Rebecca'),
    ('Jacob');

UPDATE people SET
    father = (SELECT id FROM people WHERE name = 'Abraham'),
    mother =(SELECT id FROM people WHERE name = 'Sarah')
    WHERE name = 'Isaac';

UPDATE people SET
    father = (SELECT id FROM people WHERE name = 'Abraham'),
    mother =(SELECT id FROM people WHERE name = 'Hagar')
    WHERE name = 'Ishmael';

UPDATE people SET
    father = (SELECT id FROM people WHERE name = 'Isaac'),
    mother =(SELECT id FROM people WHERE name = 'Rebecca')
    WHERE name = 'Jacob';


SELECT people.name as Name, father.name as Father, mother.name as Mother
    FROM people, people father, people mother
    WHERE father.id = people.father and mother.id = people.mother;

SELECT people.name as Name, father.name as Father, mother.name as Mother
    FROM people, people father, people mother
    WHERE father.id = people.father and mother.id = people.mother;


