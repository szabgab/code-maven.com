CREATE TABLE score (
    name TEXT UNIQUE NOT NULL,
    recent INTEGER NOT NULL
);

INSERT INTO score (name, recent) VALUES('Joe', 23)
  ON CONFLICT(name) DO UPDATE SET recent=excluded.recent;

SELECT * FROM score;

INSERT INTO score (name, recent) VALUES('Joe', 42)
  ON CONFLICT(name) DO UPDATE SET recent=excluded.recent;

SELECT * FROM score;

