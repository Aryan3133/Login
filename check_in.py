import mysql.connector
from mysql.connector import errorcode

def connect_to_server(config):
    try:
        cnx = mysql.connector.connect(**config)
        print("Connected to MySQL server")
        return cnx
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def create_database(cursor, database_name):
    try:
        cursor.execute(f"CREATE DATABASE {database_name}")
        print(f"Database '{database_name}' created successfully.")
    except mysql.connector.Error as err:
        print(f"Failed to create database '{database_name}': {err}")

def check_and_create_database(config, database_name, tables):
    cnx = connect_to_server(config)
    if cnx is None:
        return None
    
    cursor = cnx.cursor()
    try:
        cursor.execute("SHOW DATABASES LIKE %s", (database_name,))
        result = cursor.fetchone()
        if result:
            print(f"Database '{database_name}' already exists.")
            # Update config to connect to the newly created/existing database
            config['database'] = database_name
            check_and_create_tables(config, tables)
        else:
            create_database(cursor, database_name)
            # Update config to connect to the newly created/existing database
            config['database'] = database_name
            check_and_create_tables(config, tables)
    except mysql.connector.Error as err:
        print(f"Error checking database '{database_name}': {err}")
        return None
    finally:
        cursor.close()
        cnx.close()
    return config

def create_table(cursor, table_name, table_description):
    try:
        print(f"Creating table '{table_name}'...")
        cursor.execute(table_description)
        print(f"Table '{table_name}' created successfully.")
    except mysql.connector.Error as err:
        print(f"Failed to create table '{table_name}': {err}")

def check_and_create_tables(config, tables):
    cnx = connect_to_server(config)
    if cnx is None:
        return
    
    cursor = cnx.cursor()
    for table_name, table_description in tables.items():
        try:
            cursor.execute(f"DESCRIBE {table_name}")
            cursor.fetchall()  # Fetch all results to ensure the cursor is fully consumed
            print(f"Table '{table_name}' already exists.")
        except mysql.connector.Error as err:
                create_table(cursor, table_name, table_description)

    cursor.close()
    cnx.close()

config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'solo3111'
}

database_name = 'data'
tables = {
    'registration': """CREATE TABLE registration (
        user_id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        user_name VARCHAR(20) NOT NULL UNIQUE,
        name VARCHAR(40) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE,
        dob DATE NOT NULL,
        address VARCHAR(255),
        phone_no BIGINT NOT NULL UNIQUE,
        security_question VARCHAR(255) NOT NULL,
        answer VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        time DATETIME NOT NULL
    )""",

    'log': """CREATE TABLE log 
    (user VARCHAR(20) NOT NULL,
      time INT NOT NULL,
      FOREIGN KEY (user) REFERENCES registration(user_name))"""
}

check_and_create_database(config, database_name, tables)
