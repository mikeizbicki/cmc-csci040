'''
In this lab, you will create a sqlite database that will serve as the database for your twitter clone.

To complete this lab, implement the following steps and upload the resulting lab.py file to sakai.

Steps:

    1. Import sqlite and create a database called 'twitter_clone.db'

    2. Create two tables in this database

        a. The first table should be called users and have columns "username" and "password" of type text

        b. The second table should be called messages and have columns "sender" and "message" of type text, and "timestamp" of type datetime

    3. Insert 3 rows into your users table with whatever usernames and passwords you choose 

    4. Read the password from the database for a specified user and print it to the screen

    5. Insert 3 rows into the messages table; make sure that the datetime for each message is set to the current time when your computer inserts the rows

    6. Read the messages from the table and print them to the screen

'''
