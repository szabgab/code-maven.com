SELECT COUNT(*) FROM person;
SELECT "Total", COUNT(*) FROM person;
SELECT "Physycs", COUNT(*) FROM person WHERE subject == "Physics";
SELECT "Failed", COUNT(*) FROM person WHERE grade < 60;

SELECT "Maximum all", MAX(grade) FROM person;
SELECT "Maximum Chemistry", MAX(grade) FROM person WHERE subject == "Chemistry";

SELECT "Average all", AVG(grade) FROM person;
SELECT "Average Chemistry", AVG(grade) FROM person WHERE subject == "Chemistry";
SELECT "Average Physics", AVG(grade) FROM person WHERE subject == "Physics";
