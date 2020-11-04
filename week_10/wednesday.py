# this python file just creates the table schemas,
# and inserts some dummy data

# built in python3, no need to pip3 install
import sqlite3

# connect to the database
con = sqlite3.connect('wednesday.db')
cur = con.cursor()

sql = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER
);
'''
cur.execute(sql)

sql = '''
insert into users (username, password, age) values ('trump', '12345', 74);
'''
cur.execute(sql)
con.commit()

sql = '''
select * from users;
'''
cur.execute(sql)
results = cur.fetchall()
print('results=',results)
