# this python file will use/read from the database

# built in python3, no need to pip3 install
import sqlite3

# connect to the database
con = sqlite3.connect('wednesday.db')
cur = con.cursor()

#--select * from users;

# Not allowed in SQL 
# select (id,username,password,age) from users;

print('enter your usersname:')
username = input()
age = 18

# SQL injection is when a user puts sql commands into the variable that you're using to create your sql command
# a technique for breaking systems
# standard attack method, you'll want to make sure your code is not vulnerable

# use python code to generate a sql command;
# similar to using python to generate html commands, generate markdown

#sql = """
#select id,username,age,password from users where username=='""" +username+"""';
#"""
#print('sql=',sql)
#cur.execute(sql)

sql = """
select id,username,age,password from users where username==? and age>?
"""
cur.execute(sql, (username,age))

results = cur.fetchall()
print('results=',results)
for row in results:
    print('================')
    # the row variable corresponds to the rows of the table that match the select command
    print('row=',row)

    # a tuple is like a list, but with () instead of []
    print('id=', row[0])
    print('username=', row[1])
    #print('password=', row[2])
    #print('age=', row[3])
    print('password=', row[3])
    print('age=', row[2])

# format of the output of cur.fetchall()
