# Problem 4b

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

username = "example"
password = 'password'
sql = """
INSERT INTO users (username, password) VALUES ('?', ?);
"""
cur.execute(sql, [username])
con.commit()

sql = """
SELECT id,password FROM users WHERE username='?';
"""
cur.execute(sql)
for row in cur.fetchall():
   print('row[0]=', row[0])
   print('row[1]=', row[1])


