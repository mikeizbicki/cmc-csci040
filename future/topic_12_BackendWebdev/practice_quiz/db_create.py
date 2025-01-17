#!/usr/bin/python3
'''
Create a database for the Twitter project.
'''

# sqlite3 is built in python3, no need to pip3 install
import sqlite3

# process command line arguments
import argparse
parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
# there is no standard file extension; people use .db .sql .sql3 .database
args = parser.parse_args()

# connect to the database
con = sqlite3.connect(args.db_file)   # con, conn = connection; always exactly 1 of these variables per python project
cur = con.cursor()                    # cur = cursor; for our purposes, exactly 1 of these per python file

# create the users table
sql = '''
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER
);
'''
cur.execute(sql)     # cur.execute() actually runs the SQL code
con.commit()         # "commit" means "save" in SQL terminology; not always required, but never wrong

# insert some dummy data
cur.execute("insert into users (username, password, age) values ('Trump', 'Trump', 76);")
cur.execute('''insert into users (username, password, age) values ('Biden', 'Biden', 79);''')
cur.execute('''insert into users (username, password, age) values ('Evan', 'correct horse battery staple', 4);''')
cur.execute('''insert into users (username, password, age) values ('Isaac', 'soccer', 1);''')
cur.execute('''insert into users (username, password, age) values ('Aaron', 'guaguagua', 0);''')
cur.execute('''insert into users (username, password, age) values ('Mike', '524euTjrWm6uK2C5iw8mC6aNgX1JI78o', 35);''')
cur.execute('''insert into users (username, password) values ('Kristen', 'Possible-Rich-Absolute-Battle');''')
con.commit()

# create the messages table
sql = '''
create table messages (
    id integer primary key,
    sender_id integer not null,
    message text not null,
    created_at timestamp not null default current_timestamp
    );
'''
cur.execute(sql)
con.commit()

# insert some dummy data
sql = '''
insert into messages (sender_id,message,created_at) values
    (1, 'I''m a baby', '2021-11-14 14:30:00'),
    (2, 'I''m a baby', '2021-11-14 14:30:00'),
    (3, 'I''m a baby', '2021-11-14 14:33:01'),
    (4, 'I''m a baby', '2021-11-15 14:35:45');
'''
cur.execute(sql)
con.commit()

sql='''
insert into messages (sender_id,message,created_at) values
    (3, 'I''m actually a toddler', '2021-11-16 14:35:45');
'''
cur.execute(sql)
con.commit()

sql='''
insert into messages (sender_id,message,created_at) values
    (6, 'Today in 1918, the Armistice that effectively ended WWI came into effect.', '2021-11-11 11:00:00');
'''
cur.execute(sql)
con.commit()

sql='''
insert into messages (sender_id,message) values
    (6, 'I''m an adult'),
    (6, 'SQL is the best!!'),
    (7, 'I''m an adult'),
    (7, 'WTF is SQL?!  I thought you liked the snake thing.');
'''
cur.execute(sql)
con.commit()
