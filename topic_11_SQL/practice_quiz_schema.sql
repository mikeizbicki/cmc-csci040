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

insert into users (username, password, age) values ('Trump', 'TRUMP', 76);
insert into users (username, password, age) values ('Biden', '12345', 79);
insert into users (username, password, age) values ('Evan', 'correct horse battery staple', 4);
insert into users (username, password, age) values ('Isaac', 'soccer', 1);
insert into users (username, password, age) values ('Aaron', 'guaguagua', 0);
insert into users (username, password, age) values ('Mike', '524euTjrWm6uK2C5iw8mC6aNgX1JI78o', 35);
insert into users (username, password) values ('Kristen', 'Possible-Rich-Absolute-Battle');

----------------------------------------
-- messages
----------------------------------------
create table messages (
    id integer primary key,
    sender_id integer not null REFERENCES users(id),
    message text not null,
    created_at timestamp not null default current_timestamp
);

insert into messages (sender_id,message,created_at) values
    (1, 'I''m a baby', '2022-11-14 14:30:00'),
    (2, 'I''m a baby', '2022-11-14 14:30:00'),
    (3, 'I''m a baby', '2022-11-14 14:33:01'),
    (4, 'I''m a baby', '2022-11-15 14:35:45');

insert into messages (sender_id,message,created_at) values
    (3, 'I''m actually a toddler', '2022-11-16 14:35:45');
    
insert into messages (sender_id,message,created_at) values
    (6, 'I''m celebrating armistice day, not memorial day.', '2022-11-11 11:00:00');
    
insert into messages (sender_id,message,created_at) values
    (6, 'I''m an adult', '2022-11-17 14:35:25'),
    (6, 'SQL is the best!!', '2022-11-17 15:52:45'),
    (7, 'I''m an adult', '2022-11-17 16:12:21'),
    (7, 'WTF is SQL?!  I thought you liked the snake thing.', '2022-11-17 15:53:47');
