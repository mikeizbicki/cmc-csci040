#!/usr/bin/python3
'''
Output a summary of the contents of the twitter database.
'''

# sqlite3 is built in python3, no need to pip3 install
import sqlite3

# process command line arguments
import argparse
parser = argparse.ArgumentParser(description='Create a database for the twitter project')
parser.add_argument('--db_file', default='twitter_clone.db')
args = parser.parse_args()

# connect to the database
con = sqlite3.connect(args.db_file)
cur = con.cursor()

# print users
print('================================================================================')
print('users')
print('================================================================================')
# this is a python comment
sql = """
-- this is a SQL comment
select id,username,password,age from users;
"""
print('sql=',sql)
cur.execute(sql)
# there is no con.commit() because I'm not trying to save anything
for row in cur.fetchall():    # cur.fetchall() is an iterable over all the rows returned by out sql query
    # row is "like" a list in the sense that you must use indexes to get the information
    # with select *, the order of results is the same as the order from the CREATE TABLE command
    print('id=', row[0])
    print('username=', row[1])
    print('password=', row[2])
    print('age=', row[3])
    print('================')
    # all of the times doing a select, you'll follow this pattern

'''
With this CREATE TABLE command:
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER
);
For SELECT *,
row[0] is id
row[1] is username
row[2] is password
row[3] is age

With this CREATE TABLE command:
CREATE TABLE users (
    age INTEGER,
    id INTEGER PRIMARY KEY,
    password TEXT NOT NULL,
    username TEXT NOT NULL UNIQUE
);
For SELECT *,
row[0] is age
row[1] is id
row[2] is password
row[3] is username

It's recommended not to use SELECT * because the code will break if the CREATE TABLE command changes.
'''

# print messages
print('================================================================================')
print('messages')
print('================================================================================')
sql = """
select * from messages;
"""
cur.execute(sql)
for row in cur.fetchall():
    print('id=', row[0])
    print('id_sender=', row[1])
    print('message=', row[2])
    print('created_at=', row[3])
    print('================')

