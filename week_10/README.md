# Week 10: SQL

<center>
<img width='80%' src=dilbert5.jpg />
</center>

<!--
**Quiz:**
The completed `quiz.pdf` should be submitted to sakai by Friday at midnight.

https://www.tutorialspoint.com/flask/index.htm
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
-->

**Monday:**
We will go over how to use the sqlite3 database.
We will cover the following sql commands:

1. CREATE: https://www.w3schools.com/sql/sql_create_table.asp

1. INSERT: https://www.w3schools.com/sql/sql_insert.asp

1. SELECT: https://www.w3schools.com/sql/sql_select.asp

1. UPDATE: https://www.w3schools.com/sql/sql_update.asp

1. DELETE: https://www.w3schools.com/sql/sql_delete.asp

Optional task:

1. Download and install the sqlite3 executable for your computer at: https://www.sqlitetutorial.net/download-install-sqlite/

Note:

1. SQL is extremely widely used in data analysis.
   If you take CS36 (Foundations of Data Science) or CS143 (Big Data),
   you will learn significantly more advanced SQL.

**Wednesday:**
We will go over how to use sqlite3 within python.
The following tutorial will be your reference material:

1. https://stackabuse.com/a-sqlite-tutorial-with-python/

## Lab

Create 2 python files:

1. The `create_db.py` file will contain the SQL commands to create a database file called `database.db`.
   It should create two tables with the following schemas:
   ```
    create table users (
        id integer primary key,
        username text not null unique,
        password text not null,
        age integer
        );
    create table messages (
        id integer primary key,
        sender_id integer not null,
        message text not null,
        created_at timestamp not null default current_timestamp
        );
    ```
    Then, it should insert 3 example users and 5 example messages using the `insert` command.

    HINT:
    This file follows the format of the `wednesday.py` file in the lecture notes.

    HINT:
    Don't forget to run the `con.commit()` function after running your `insert` statements like I did in class.

1. The `access_db.py` file should use the `select` statement to print all the contents of both the `users` and `messages` tables within the `database.db` database file.

   HINT:
   This file follows the format of the `wednesday_access.py` file from the lecture notes.

Submit your 2 python files and your db file to sakai.
