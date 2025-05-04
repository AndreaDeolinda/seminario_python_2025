	
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    pass VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
);

INSERT INTO users (username, pass) VALUES ('user1', 'password1');
INSERT INTO users (username, pass) VALUES ('user2', 'password2');
INSERT INTO users (username, pass) VALUES ('user3', 'password3');




SELECT * FROM users;

		



