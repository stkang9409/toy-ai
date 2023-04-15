import logging
import os
import mysql.connector

# MYSQL_HOST = os.environ["MYSQL_HOST"]
# MYSQL_USER = os.environ["MYSQL_USER"]
# MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
# MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'secret'
MYSQL_DATABASE = 'mydatabase'


def get_db_connection():
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE,
    )
    return connection


def create_image_table():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS images (
            id INT AUTO_INCREMENT PRIMARY KEY,
            image_url VARCHAR(255) NOT NULL
        )
        '''
        cursor.execute(create_table_query)
        connection.commit()

        logging.info("Table 'images' created.") 

    except mysql.connector.Error as error:
        logging.info(f"Error creating table: {error}")
    

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

    logging.info("Table 'images' created successfully.")



def table_exists(table_name):
    connection = get_db_connection()
    cursor = connection.cursor()

    check_table_query = f'''
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = '{MYSQL_DATABASE}' AND table_name = '{table_name}'
    '''

    cursor.execute(check_table_query)
    result = cursor.fetchone()
    table_exists = result[0] == 1

    print(f"Result of the query: {result}")  # Add this print statement
    print(f"Table exists: {table_exists}")

    cursor.close()
    connection.close()

    return table_exists


def insert_image_url(image_url):
    connection = get_db_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO images (image_url) VALUES (%s)"
    data = (str(image_url),)

    cursor.execute(insert_query, data)
    connection.commit()

    cursor.close()
    connection.close()