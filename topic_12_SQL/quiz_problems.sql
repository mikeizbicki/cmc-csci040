/*
 * For each problem below, write the output of the SQL SELECT statement.
 * If there is no output, write "No Output".
 * There should be no errors given by any of these problems.
 */

----------------------------------------
-- Problem 1
----------------------------------------

SELECT count(*) FROM messages WHERE message LIKE '%baby%';




----------------------------------------
-- Problem 2
----------------------------------------

SELECT id FROM users WHERE username = 'Aaron';




----------------------------------------
-- Problem 3
----------------------------------------

SELECT count(*) FROM messages WHERE sender_id=6;





----------------------------------------
-- Problem 4
----------------------------------------

DELETE FROM messages WHERE sender_id=3 OR sender_id=0;
SELECT count(*) FROM messages;
