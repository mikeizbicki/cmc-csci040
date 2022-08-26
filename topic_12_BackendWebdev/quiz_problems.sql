/*
 * Each problem below assumes the attached schema.sql file has been run.
 * For each problem, write the output of the SQL SELECT statement.
 * If there is no output, write "No Output".
 * Each problem is worth 2 points.
 */

----------------------------------------
-- Problem 1
----------------------------------------

SELECT age FROM users WHERE username LIKE 'BIDEN';




----------------------------------------
-- Problem 2
----------------------------------------

SELECT id FROM users WHERE username LIKE 'a' ORDER BY username ASC;




----------------------------------------
-- Problem 3
----------------------------------------

SELECT count(*) FROM users WHERE age<18;




----------------------------------------
-- Problem 4
----------------------------------------

SELECT id
FROM messages
WHERE sender_id=3
   OR sender_id=2
ORDER BY created_at DESC;




----------------------------------------
-- Problem 5
----------------------------------------

SELECT count(*) FROM messages WHERE message LIKE '%''%'; 
