# RDBMS
# ACID
# CRUD Create Read Update Destroy
# Declarative: HTML, SQL
# Imperative: Python, C++, Java
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

# INSERT, UPDATE, DELETE
# need to call connection.commit()
username='Bernie'
password='password'
sql = '''
INSERT INTO users(username,password)
VALUES (?,?);
'''
cursor.execute(sql,[username,password])
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



