'''
In this lab, you will create a sqlite database that will serve as the database for your twitter clone.

To complete this lab, implement the following steps in this lab.py file:

    1. Import sqlite and create a database called 'twitter_clone.db'

    2. Create two tables in this database

        a. The first table should be called users and have columns "username" and "password" of type text, and the username column should have a unique constraint

        b. The second table should be called messages and have columns "sender" and "message" of type text, and "timestamp" of type datetime

    3. Insert 3 rows into your users table with whatever usernames and passwords you choose 

    4. Verify that your unique constraint on username works by trying to insert a duplicate username; sqlite should throw an exception, and you must catch the exception so that your program does not crash.

    5. For a particular user X that you just added:

        a. Select the user's password from the database and print it to the screen

        b. Update the password for the user

        c. Repeat step 5.a

    6. Insert 3 rows into the messages table, one for each user; make sure that the datetime for each message is set to the current time when your computer inserts the rows

    7. Read all the messages from the table and print them to the screen, including the sender and the timestamp

    8. Delete the message from one of the users

    9. Repeat step 7

Upload the lab.py file and the output of your program to sakai.

'''
