/*
 * For each problem below, write the output of the SQL SELECT statement.
 * If there is no output, write "No Output".
 * There should be no errors given by any of these problems.
 * Your quiz will have 5 problems in a similar format.
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

SELECT id FROM users WHERE username = NULL;




----------------------------------------
-- Problem 6
----------------------------------------

SELECT id FROM users ORDER BY username DESC;




----------------------------------------
-- Problem 7
----------------------------------------

SELECT id FROM users ORDER BY age ASC;




----------------------------------------
-- Problem 8
----------------------------------------

SELECT id FROM users ORDER BY username ASC;




----------------------------------------
-- Problem 9
----------------------------------------

SELECT count(*) FROM messages WHERE sender_id=4;




----------------------------------------
-- Problem 10
----------------------------------------

SELECT count(*) FROM messages;






----------------------------------------
-- Problem 11
----------------------------------------

SELECT count(*) FROM messages WHERE sender_id < 4;






----------------------------------------
-- Problem 12
----------------------------------------

DELETE FROM messages;
SELECT count(*) FROM messages;




----------------------------------------
-- Problem 13
----------------------------------------

DELETE FROM messages WHERE sender_id=1;
SELECT count(*) FROM messages;





----------------------------------------
-- Problem 14
----------------------------------------

DELETE FROM messages WHERE message LIKE '%a%';
SELECT count(*) FROM messages;





----------------------------------------
-- Problem 15
----------------------------------------

DELETE FROM messages WHERE sender_id=3 OR sender_id=0;
SELECT count(*) FROM messages;




----------------------------------------
-- Problem 16
----------------------------------------

UPDATE users SET password='@realdonaldtrump';
SELECT count(*) FROM users WHERE password LIKE '@%';






----------------------------------------
---- Problem 17
------------------------------------------

UPDATE users SET username='@realdonaldtrump' WHERE id=1;
SELECT count(*) FROM users WHERE username LIKE '@%';





