/*
 * This file is the leftmost pane in <https://sqlite.org/fiddle/>
 */

.mode markdown

----------------------------------------
-- users
----------------------------------------

CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    age INTEGER
);

INSERT INTO users (username, password, age) VALUES ('Trump', 'TRUMP', 76);
INSERT INTO users (username, password, age) VALUES ('Biden', '12345', 79);
INSERT INTO users (username, password, age) VALUES ('Evan', 'correct horse battery staple', 7);
INSERT INTO users (username, password, age) VALUES ('Isaac', 'soccer', 4);
INSERT INTO users (username, password, age) VALUES ('Aaron', 'guaguagua', 3);
INSERT INTO users (username, password, age) VALUES ('Aurelia', '', 2);
INSERT INTO users (username, password, age) VALUES ('Mike', '524euTjrWm6uK2C5iw8mC6aNgX1JI78o', 38);
INSERT INTO users (username, password) VALUES ('Kristen', 'Possible-Rich-Absolute-Battle');

----------------------------------------
-- messages
----------------------------------------

create table messages (
    id integer primary key,
    sender_id integer not null references users(id),
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
    (6, 'Today in 1918, the Armistice that effectively ended WWI came into effect.', '2022-11-11 11:00:00');
    
insert into messages (sender_id,message,created_at) values
    (6, 'I''m an adult', '2022-11-17 14:35:25'),
    (6, 'SQL is the best!!', '2022-11-17 15:52:45'),
    (7, 'I''m an adult', '2022-11-17 16:12:21'),
    (7, 'WTF is SQL?!  I thought you liked the snake thing.', '2022-11-17 15:53:47');

----------------------------------------
-- copy/paste the problem below here
----------------------------------------
