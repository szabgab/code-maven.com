CREATE TABLE person (
    name TEXT,
    subject TEXT,
    grade INTEGER
);

INSERT INTO person (name, subject, grade) VALUES ('Jane',  'Chemistry', 62);
INSERT INTO person (name, subject, grade) VALUES ('Jane',  'Physics', 70);
INSERT INTO person (name, subject, grade) VALUES ('Joe',   'Chemistry', 45);
INSERT INTO person (name, subject, grade) VALUES ('Joe',   'Physics', 85);
INSERT INTO person (name, subject, grade) VALUES ('Peter', 'Chemistry', 35);
INSERT INTO person (name, subject, grade) VALUES ('Peter', 'Physics', 63);
INSERT INTO person (name, subject, grade) VALUES ('Mary',  'Chemistry', 95);
INSERT INTO person (name, subject, grade) VALUES ('Dean', 'Physics', 100);

SELECT COUNT(*) FROM person;
SELECT "Total", COUNT(*) FROM person;
SELECT "Physycs", COUNT(*) FROM person WHERE subject == "Physics";
SELECT "Failed", COUNT(*) FROM person WHERE grade < 60;

SELECT "Maximum all", MAX(grade) FROM person;
SELECT "Maximum Chemistry", MAX(grade) FROM person WHERE subject == "Chemistry";

SELECT "Average all", AVG(grade) FROM person;
SELECT "Average Chemistry", AVG(grade) FROM person WHERE subject == "Chemistry";
SELECT "Average Physics", AVG(grade) FROM person WHERE subject == "Physics";
