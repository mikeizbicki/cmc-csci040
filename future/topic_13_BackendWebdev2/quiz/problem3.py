# Problem 3

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

