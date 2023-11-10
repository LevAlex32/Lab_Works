db_blog=> SELECT username FROM users WHERE LENGTH(username)<8;

db_blog=> SELECT * FROM users WHERE id >2 AND email LIKE '%@yandex.ru';

db_blog=> SELECT comment, username FROM comments, users WHERE artivle_id BETWEEN 2 AND 3 AND users.username IN ('Traveler');

db_blog=> SELECT username, id FROM users ORDER BY id DESC;
 
