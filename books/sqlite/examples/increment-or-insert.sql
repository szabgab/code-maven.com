CREATE TABLE counters (
    name UNIQUE NOT NULL,
    number INTEGER NOT NULL
);

INSERT INTO counters (name, number)
  VALUES ('apple', 1)
  ON CONFLICT(name) DO UPDATE SET number = number + 1;

SELECT * FROM counters;

INSERT INTO counters (name, number)
  VALUES ('apple', 1)
  ON CONFLICT(name) DO UPDATE SET number = number + 1;

SELECT * FROM counters;

