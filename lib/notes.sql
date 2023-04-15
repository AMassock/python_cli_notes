BEGIN;

SET client_encoding = 'LATIN1';

CREATE TABLE note (
    title varchar NOT NULL,
    body text
);

INSERT INTO note
(title, body)
VALUES('Test 1', 'This is the first entry into the notes DB'),
('Test 2', 'This is the second entry into the notes DB'),
('Test 3', 'This is the third entry into the notes DB'),
('Test 4', 'Can you tell I am super creative?');

COMMIT;