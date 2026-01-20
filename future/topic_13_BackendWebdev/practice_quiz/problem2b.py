# Problem 2b

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

sql = """
INSERT INTO users (username, password, age) VALUES ('example', 'password', 22);
"""
cur.execute(sql)
con.commit()

sql = """
SELECT password,id FROM users WHERE username='example';
"""
cur.execute(sql)
for row in cur.fetchall():
   print('row[0]=', row[0])
   print('row[1]=', row[1])

