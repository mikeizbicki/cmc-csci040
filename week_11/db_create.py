# this python file just creates the table schemas,
# and inserts some dummy data

# built in python3, no need to pip3 install
import sqlite3

# connect to the database
con = sqlite3.connect('twitter_clone.db')
cur = con.cursor()

# create the users table
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
insert into users (username, password, age) values 
    ('trump', '12345', 74),
    ('biden', 'password', 77),
    ('evan', 'asd9uh9893dsdASDas-d', 2);
'''
cur.execute(sql)
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

sql = '''
insert into messages (sender_id, message) values 
    (1, 'I''m a baby.'),
    (2, 'I''m a baby.'),
    (3, 'I''m a toddler.'),
    (3, 'My daddy is the best.'),
    (3, 'I love you, I love everyone :)');
'''
cur.execute(sql)
con.commit()
