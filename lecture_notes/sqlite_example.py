import sqlite3

connection = sqlite3.connect('webpage_database2.db')
cursor = connection.cursor()

sql = '''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER,
    username TEXT,
    password TEXT,
    PRIMARY KEY(id)
);
'''
cursor.execute(sql)

sql = '''
INSERT INTO users(username,password)
VALUES ('Bernie','password');
'''
cursor.execute(sql)
connection.commit()

user='Trump'
sql = '''
SELECT * FROM users WHERE username=?;
'''
res = cursor.execute(sql,[user])
rows = res.fetchall()
if rows == []:
    print('username not in users')
else:
    for row in rows:
        print('row=',row)



