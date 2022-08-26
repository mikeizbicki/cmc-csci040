/*
 * This file is the leftmost pane in https://SQLFiddle.com
 */

----------------------------------------
-- users
----------------------------------------
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER
);

insert into users (username, password, age) values ('Trump', 'TRUMP', 75);
insert into users (username, password, age) values ('Biden', 'Biden', 78);
insert into users (username, password, age) values ('Evan', 'correct horse battery staple', 3);
insert into users (username, password, age) values ('Isaac', 'guaguagua', 0);
insert into users (username, password, age) values ('Mike', '524euTjrWm6uK2C5iw8mC6aNgX1JI78o', 35);
insert into users (username, password) values ('Kristen', 'Possible-Rich-Absolute-Battle');

----------------------------------------
-- messages
----------------------------------------
create table messages (
    id integer primary key,
    sender_id integer not null,
    message text not null,
    created_at timestamp not null default current_timestamp
);

insert into messages (sender_id,message,created_at) values
    (1, 'I''m a baby', '2021-11-14 14:30:00'),
    (2, 'I''m a baby', '2021-11-14 14:30:00'),
    (3, 'I''m a baby', '2021-11-14 14:33:01'),
    (4, 'I''m a baby', '2021-11-15 14:35:45');

insert into messages (sender_id,message,created_at) values
    (3, 'I''m actually a toddler', '2021-11-16 14:35:45');
    
insert into messages (sender_id,message,created_at) values
    (5, 'I''m celebrating armistice day, not memorial day.', '2021-11-11 11:11:11');
    
insert into messages (sender_id,message,created_at) values
    (5, 'I''m an adult', '2021-11-17 14:35:25'),
    (5, 'SQL is the best!!', '2021-11-17 15:52:45'),
    (6, 'I''m an adult', '2021-11-17 16:12:21'),
    (6, 'WTF is SQL?!  I thought you liked the snake thing.', '2021-11-17 15:53:47');
