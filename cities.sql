USE hbnb_dev_db;  -- Specify the database to use

-- Your SQL commands for creating the cities table
CREATE TABLE cities (
    id INT NOT NULL AUTO_INCREMENT,
    created_at DATETIME NOT NULL, 
    updated_at DATETIME NOT NULL, 
    name VARCHAR(128) NOT NULL, 
    state_id INT NOT NULL,  -- Change the data type to INT to match the referenced column
    PRIMARY KEY (id), 
    FOREIGN KEY (state_id) REFERENCES states (id)
);

