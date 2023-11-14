db_blog=> SELECT comment FROM comments WHERE user_id >= (
		SELECT MAX(user_id) FROM comments);

db_blog=> SELECT article.id, article.content, COUNT(comments.comment) 
	  	FROM article LEFT JOIN comments ON article.id = comments.artivle_id 
		GROUP BY article.id;

db_blog=> SELECT users.id, username, email, COUNT(article.id) FROM users 
		LEFT JOIN article ON users.id = article.author_id 
		GROUP BY users.id, article.id, username,email 
		HAVING article.id <= 1;

