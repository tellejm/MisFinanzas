CREATE TABLE IF NOT EXISTS users(
    id NOT NULL AUTO_INCREMENT UNIQUE,
    username VARCHAR(30) NOT NULL UNIQUE,
    name VARCHAR(30) NOT NULL,
    lastname VARCHAR(30) NOT NULL,
    password VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL,
    address VARCHAR(30) NOT NULL,
    birth_date DATE,
    gender ENUM('Masculino', 'Femenino', 'Prefiero no decirlo', 'Otro'),
    work_status ENUM('Empleado', 'Indepemdiente', 'Desempleado'),
    PRIMARY KEY (id)
);

CREATE TALBE IF NOT EXISTS account_type(
    id NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(30) NOT NULL,
    description TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS accounts(
    id NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(30) NOT NULL,
    account_type_id INT NOT NULL,
    description TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (account_type_id) REFERENCES account_type(id)
);

CREATE TABLE IF NOT EXISTS account_has_user(
    account_id INT NOT NULL,
    user_id INT NOT NULL,
    PRIMARY KEY (account_id, user_id),
    FOREIGN KEY (account_id) REFERENCES accounts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS movements(
    id AUTO_INCREMENT UNIQUE NOT NULL,
    user_id INT NOT NULL,
    account_id INT NOT NULL,
    value BIGINT NOT NULL,
    date DATE NOT NULL,
    description TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (account_id) REFERENCES accounts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS calendar (
    id NOT NULL AUTO_INCREMENT UNIQUE,
    user_id INT NOT NULL,
    account_id INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    recursive BOOLEAN NOT NULL DEFAULT 0,
    value BIGINT NOT NULL,
    description TEXT,
    PRIMARY KEY (id),
    FOREIGN KEY (account_id) REFERENCES accounts(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);