import os
import mysql.connector

MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]

# MYSQL_HOST = 'db'
# MYSQL_USER = 'root'
# MYSQL_PASSWORD = 'secret'
# MYSQL_DATABASE = 'mydatabase'


def get_db_connection():
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    return connection