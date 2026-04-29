# Problem 6c

import sqlite3

con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

username = "Mike' OR username='Trump"
sql = """
SELECT id FROM users WHERE username='""" + username + """';
"""
cur.execute(sql)
user_ids = []
for row in cur.fetchall():
    user_ids.append(row[0])

for user_id in user_ids:
    sql = """
    SELECT id, sender_id, message, created_at FROM messages WHERE sender_id=""" + str(user_id) + """;
    """
    cur.execute(sql)
    for row in cur.fetchall():
        print('id=', row[0], 'sender_id=', row[1], 'message=', row[2], 'created_at=', row[3])
