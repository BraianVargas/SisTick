CREATE DATABASE sictick;
USE sictick;

CREATE TABLE usuarios (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    type ENUM('admin', 'usuario') NOT NULL
);

CREATE TABLE tickets (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    creator_id INT(11) NOT NULL,
    assigned_to INT(11) NOT NULL,
    state ENUM('abierto', 'en progreso', 'cerrado') NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (creator_id) REFERENCES usuarios(id),
    FOREIGN KEY (assigned_to) REFERENCES usuarios(id)
);

CREATE TABLE comentarios (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT(11) NOT NULL,
    user_id INT(11) NOT NULL,
    content TEXT NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES tickets(id),
    FOREIGN KEY (user_id) REFERENCES usuarios(id)
);

CREATE TABLE historial (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT(11) NOT NULL,
    user_id INT(11) NOT NULL,
    action VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    FOREIGN KEY (ticket_id) REFERENCES tickets(id),
    FOREIGN KEY (user_id) REFERENCES usuarios(id)
);