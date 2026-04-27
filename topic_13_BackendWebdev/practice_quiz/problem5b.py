# Problem 5b

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

username = "Mike' OR username='Trump"
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

