'''
Instructions:
For each problem below, write the output of all print functions.
You may use any handwritten/printed notes,
but may not use a computer.
If a print function never gets called, then do not write anything.
If it gets called more than once, then write the output for each time it is called.

Recall that each problem is independent of the others.
For example, if a row is inserted in Problem 1,
it will not be available in Problem 2.
'''

########################################
# Problem 1
########################################

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()
sql = """
SELECT count(*) FROM messages WHERE message LIKE '%baby%';
"""
cur.execute(sql)
for row in cur.fetchall():
   print('row[0]=', row[0])



########################################
# Problem 2
########################################

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

username = "example', 'password'), ('example2"
password = 'password'
sql = """
INSERT INTO users (username, password) VALUES ('"""+username+"""', '"""+password+"""');
"""
cur.execute(sql)
con.commit()

sql = """
SELECT id,password FROM users WHERE username LIKE 'example%';
"""
cur.execute(sql)
for row in cur.fetchall():
   print('row[0]=', row[0])
   print('row[1]=', row[1])




########################################
# Problem 3
########################################

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

username = "Aaron' OR username='Isaac"
sql = """
SELECT id,password FROM users WHERE username='"""+ username +"""';
"""
cur.execute(sql)
user_ids = []
for row in cur.fetchall():
    user_ids.append(row[0])

for user_id in user_ids:
    sql = """
    SELECT count(*) FROM messages WHERE sender_id=?;
    """
    cur.execute(sql, [user_id])
    for row in cur.fetchall():
        print('row[0]=', row[0])




########################################
# Problem 4
########################################

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

username = "Aaron' OR username='Isaac"
sql = """
SELECT id,password FROM users WHERE username=?;
"""
cur.execute(sql, [username])
user_ids = []
for row in cur.fetchall():
    user_ids.append(row[0])

for user_id in user_ids:
    sql = """
    SELECT count(*) FROM messages WHERE sender_id=?;
    """
    cur.execute(sql, [user_id])
    for row in cur.fetchall():
        print('row[0]=', row[0])
