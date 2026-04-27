# Problem 1b

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()
sql = """
SELECT count(*) FROM messages WHERE message LIKE '%a%';
"""
cur.execute(sql)
for row in cur.fetchall():
   print('row[0]=', row[0])
