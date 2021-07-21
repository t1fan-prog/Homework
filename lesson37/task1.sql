CREATE TABLE users_1 (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(55), password VARCHAR(16));
ALTER TABLE users_1 RENAME TO users;
ALTER TABLE users ADD COLUMN is_paid VARCHAR(5);
INSERT INTO users (name, password, is_paid) VALUES ('Jack', 'uiashfoahs8', 'True');
INSERT INTO users (name, password, is_paid) VALUES ('Dick', 'sadiughsa78', 'False');
UPDATE users SET is_paid='False' WHERE id=1;
UPDATE users SET is_paid='True' WHERE id=2;
DELETE FROM users WHERE is_paid='False';
