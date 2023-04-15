
import logging
from core.dalle.dalle import fetch_image, fetch_image2
import os
from common.utill.db import get_db_connection, create_image_table, table_exists, insert_image_url
from flask import Flask, request, session, jsonify
from core.chatGPT.chatGPT import main, book_create
from common.utill.session_user import set_user, get_user
from common.utill.response_type import success_response
import sys



app = Flask(__name__)

@app.route('/<user_UUID>', methods=['GET'])
def main_page(user_UUID):
    set_user(user_UUID)
    return success_response({"user": get_user()})


# [테스트]
@app.route('/book', methods=['POST'])
def create_book():
    params = request.get_json()
    book = params['book']
    return success_response({"result": book_create(book)})

@app.route('/dalle', methods=['GET'])
def dalle():
    resImage = fetch_image2()
    return resImage
    

@app.route('/test')
def test():
    msg = main()
    return msg 

# [테스트]
# @app.route('/db', methods=['GET'])
# def db_test():
#     connection = get_db_connection()
#     cursor = connection.cursor()
    
#     # Example query: get the MySQL server version
#     cursor.execute("SELECT VERSION()")
#     result = cursor.fetchone()
    
#     connection.close()
#     return jsonify({"mysql_version": result[0]})

# @app.route('/tables/<table_name>', methods=['GET'])
# def check_table(table_name):
#     exists = table_exists(table_name)
#     return jsonify({"table_name": table_name, "exists": exists})


@app.route('/images', methods=['POST'])
def add_image():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        print('[분석] data ########')
        logging.info(data)
        print(data)
        if data:
            dalleResponse = fetch_image(data)
            print('This is dalleReponse #########')
            print(dalleResponse,file=sys.stdout)
            logging.info(dalleResponse)
            print(dalleResponse["data"][0]['url'])
            insert_image_url(dalleResponse["data"][0]['url'])
            return jsonify({'status': 'success', 'message': 'Image URL added successfully', 'image_url':dalleResponse["data"][0]['url']})
        else:
            return jsonify({'status': 'error', 'message': 'Image URL missing from request body'})
    else:
        return jsonify({'status': 'error', 'message': 'Invalid request method'})



if __name__ == '__main__':
    create_image_table()
    app.secret_key = 'secret-key'
    app.run(debug=True, host='0.0.0.0', port=80)


