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
sql = """
select * from users;
"""
cur.execute(sql)
for row in cur.fetchall():
    print('id=', row[0])
    print('username=', row[1])
    print('password=', row[2])
    print('age=', row[3])
    print('================')

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

