CREATE TABLE login (
    uid INTEGER NOT NULL,
    logged_in DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO login (uid) VALUES (1);
INSERT INTO login (uid, logged_in) VALUES (2, '2026-04-29 08:06:36');

SELECT * from login;
