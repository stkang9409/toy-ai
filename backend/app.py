from flask import Flask, jsonify
from core.chatGPT.chatGPT import main
from core.dalle.dalle import fetch_image
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dalle')
def dalle():
    resImage = fetch_image()
    return resImage

@app.route('/test')
def test():
    msg = main()
    return msg 

import mysql.connector

MYSQL_HOST = os.environ["MYSQL_HOST"]
MYSQL_USER = os.environ["MYSQL_USER"]
MYSQL_PASSWORD = os.environ["MYSQL_PASSWORD"]
MYSQL_DB = os.environ["MYSQL_DB"]
def get_db_connection():
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )
    return connection

@app.route('/db')
def db_test():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Example query: get the MySQL server version
    cursor.execute("SELECT VERSION()")
    result = cursor.fetchone()
    
    connection.close()
    return jsonify({"mysql_version": result[0]})

app.run(debug=True, host='0.0.0.0', port=80)


