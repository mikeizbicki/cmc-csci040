# SQL

<img width=500px src=img/dilbert5.jpg />

So far we've seen two types of languages:

1. **Procedural**: Python, Shell (sometimes called Bash/Zsh)

    Tell the computer step by step exactly HOW to accomplish ANY TASK.
    The instructions are STEP-BY-STEP.

1. **Markup**: HTML/CSS, Markdown

    Tell the computer WHAT to DISPLAY, and the computer figures out HOW to do it.

1. **Data Definition**: CSV, JSON/YAML/TOML

    Tell the computer WHAT data to STORE, but don't do anything with it.

1. **Query**: CSS Selector, Regex, Glob

    Tell the computer WHAT information to FIND.

SQL is an example of a **declarative** language.
In SQL, you tell the computer WHAT to COMPUTE,
and the computer figures out HOW automatically.

<img width=500px src=img/quote.jpg />

SQL is arguably the most important language for data scientists.
For example:

1. All interactive webpages use a SQL database to store user content.
    Data scientists run SQL code to extract and process this information.

1. Most technical interviews will do advanced SQL problems.
    To get a job as a data scientist, you'll have to write SQL code live in front of your future boss.

    In this class, we won't cover advanced SQL concepts.
    (That will be covered in CSCI143.)
    Instead, we'll be covering how to connect SQL to Python...
    basically the "why should I care" aspect of SQL.

You'll need to know the following SQL commands:

1. CREATE: <https://www.w3schools.com/sql/sql_create_table.asp>

1. INSERT: <https://www.w3schools.com/sql/sql_insert.asp>

1. SELECT: <https://www.w3schools.com/sql/sql_select.asp>
    1. WHERE <https://www.w3schools.com/sql/sql_where.asp>
    1. JOIN <https://www.w3schools.com/sql/sql_join_inner.asp>

1. UPDATE: <https://www.w3schools.com/sql/sql_update.asp>

1. DELETE: <https://www.w3schools.com/sql/sql_delete.asp>

How to run quiz problems:
```
$ pip3 install litecli
$ litecli quiz.db < quiz_schema.sql
$ litecli quiz.db
quiz.db> /* enter problem here */
```

> **NOTE:**
> If a problem runs DELETE/UPDATE on the database,
> you will need to delete and recreate the database before the next problem.
> You can use the commands:
> ```
> $ rm quiz.db
> $ litecli quiz.db < quiz_schema.sql
> ```

<!--
We'll use the following reference for connecting SQL to python:

1. <https://stackabuse.com/a-sqlite-tutorial-with-python/>
-->
