/*
 * For each problem below, write the output of the SQL SELECT statement.
 * If there is no output, write "No Output".
 * There should be no errors given by any of these problems.
 * Your quiz will have 4 problems, each worth 2 points.
 */

----------------------------------------
-- Problem 1
----------------------------------------

SELECT id FROM users WHERE username = 'Trump';




----------------------------------------
-- Problem 2
----------------------------------------

SELECT id FROM users WHERE username = 'trump';




----------------------------------------
-- Problem 3
----------------------------------------

SELECT id FROM users WHERE username LIKE 'trump';




----------------------------------------
-- Problem 4
----------------------------------------

SELECT id FROM users WHERE username LIKE 'trump';




----------------------------------------
-- Problem 5
----------------------------------------

SELECT id FROM users WHERE username LIKE 'a%';




----------------------------------------
-- Problem 6
----------------------------------------

SELECT id FROM users WHERE username LIKE '%a';




----------------------------------------
-- Problem 7
----------------------------------------

SELECT id FROM users WHERE username LIKE '%a%';




----------------------------------------
-- Problem 8
----------------------------------------

SELECT id FROM users WHERE age IS NULL;




----------------------------------------
-- Problem 9
----------------------------------------

SELECT id FROM users ORDER BY username DESC;




----------------------------------------
-- Problem 10
----------------------------------------

SELECT id FROM users ORDER BY age ASC;




----------------------------------------
-- Problem 11
----------------------------------------

SELECT id FROM users ORDER BY username ASC;




----------------------------------------
-- Problem 12
----------------------------------------

SELECT count(*) FROM messages;




----------------------------------------
-- Problem 13
----------------------------------------

SELECT count(*) FROM messages WHERE sender_id=4;





----------------------------------------
-- Problem 14
----------------------------------------

SELECT count(*) FROM messages WHERE sender_id < 4;






----------------------------------------
-- Problem 15
----------------------------------------

DELETE FROM messages;
SELECT count(*) FROM messages;




----------------------------------------
-- Problem 16
----------------------------------------

DELETE FROM messages WHERE sender_id=1;
SELECT count(*) FROM messages;





----------------------------------------
-- Problem 17
----------------------------------------

DELETE FROM messages WHERE message LIKE '%a%';
SELECT count(*) FROM messages;





----------------------------------------
-- Problem 18
----------------------------------------

DELETE FROM messages WHERE sender_id=3 OR sender_id=0;
SELECT count(*) FROM messages;




----------------------------------------
-- Problem 19
----------------------------------------

UPDATE users SET password='@realdonaldtrump';
SELECT count(*) FROM users WHERE password LIKE '@%';






----------------------------------------
---- Problem 20
------------------------------------------

UPDATE users SET username='@realdonaldtrump' WHERE id=1;
SELECT count(*) FROM users WHERE username LIKE '@%';
