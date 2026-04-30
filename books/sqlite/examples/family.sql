PRAGMA foreign_keys = ON;

CREATE TABLE people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    father INTEGER,
    mother INTEGER,
    FOREIGN KEY (father) REFERENCES people(id),
    FOREIGN KEY (mother) REFERENCES people(id)
);

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

UPDATE people SET father = 32;

SELECT child.name as Name, father.name as Father, mother.name as Mother
    FROM people child, people father, people mother
    WHERE father.id = child.father and mother.id = child.mother
    ORDER BY child.id;

-- SELECT child.name AS Name,
--        IFNULL(father.name, 'NULL') AS Father,
--        IFNULL(mother.name, 'NULL') AS Mother
--     FROM people AS child
--     LEFT JOIN people AS father ON father.id = child.father
--     LEFT JOIN people AS mother ON mother.id = child.mother
--     ORDER BY child.id;

-- CREATE VIEW family AS
--   SELECT child.name AS Name,
--          IFNULL(father.name, 'NULL') AS Father,
--          IFNULL(mother.name, 'NULL') AS Mother
--       FROM people AS child
--       LEFT JOIN people AS father ON father.id = child.father
--       LEFT JOIN people AS mother ON mother.id = child.mother
--       ORDER BY child.id;
--
-- SELECT * FROM family;

-- INSERT INTO people (name) VALUES ('Gabor');
-- SELECT * FROM family;

