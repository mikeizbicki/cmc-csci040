# Problem 2

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

sql = """
INSERT INTO users (password, username) VALUES ('example', 'password');
"""
cur.execute(sql)
con.commit()

sql = """
SELECT password,username FROM users WHERE username='password';
"""
cur.execute(sql)
for row in cur.fetchall():
   print('row[0]=', row[0])
   print('row[1]=', row[1])

