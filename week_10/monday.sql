-- comments in sql start with --
-- sql files always end in .sql; they are instructions for creating the database; human readable
-- .db files contain the result of running sql commands; they ARE the database; only machine readable, not human readable

-- # comment in python

-- the users

-- create table users (id integer, username text, age integer);

-- in the first parenthesis is the names of the columns
-- secnod set of parenthesis is the actual values
--insert into users (id, username, age) values (0, 'trump', 74);
--insert into users (id, username, age) values (1, 'biden', 77);
--insert into users (id, username, age) values (2, 'evan', 2);
--insert into users (id, username, age) values (3, 'mike', 35);

-- vocab words:
-- every table should have a primary key
-- "null value" is a value that hasn't been entered
-- the schema of a table is everything between the parenethesis of create table

create table users (
    id integer primary key,
    username text not null unique,
    age integer
    );
insert into users (username, age) values ('trump', 74);
insert into users (username, age) values ('biden', 77);
insert into users (username, age) values ('evan', 2);
insert into users (username, age) values ('mike', 35);
insert into users (username) values ('kristen'); -- age is called a "null value"

-- whenever everything works correctly, there is no ouput from a .sql file


-- DANGER!!!!
-- update and delete are both very dangerous

create table messages (
    id integer primary key,
    sender_id integer not null,
    message text not null,
    created_at timestamp not null default current_timestamp
    );

-- once you've created a table, you "can't" change the schema

insert into messages (sender_id,message) values
    (2, 'I''m actually a toddler');

insert into messages (sender_id,message,created_at) values
    (2, 'I''m a baby', '2020-11-02 14:30:00'),
    (0, 'I''m a baby', '2020-11-02 14:33:01'),
    (1, 'I''m a baby', '2020-11-02 14:35:45');
    
--id	sender_id	message	created_at
--0	2	I’m a baby	2020-11-02 14:30:00
--1	0	I’m a baby	2020-11-02 14:33:01
--2	1	I’m a baby	2020-11-02 14:35:45
--3	2	I’m actually a toddler	2020-11-02 14:42:45
