import logging

from flask import Flask, request, g
from flask_cors import CORS

from service.book_service import *
from common.config.load_config import get_flask_secret_key
from common.util.session_user import set_user, get_user
from common.util.response_type import success_response
from common.util.dbModule import init_db


app = Flask(__name__)
# init singleton DB connection
with app.app_context():
    init_db()


@app.route('/<user_UUID>', methods=['GET'])
def main_page(user_UUID):
    set_user(user_UUID)
    return success_response({"user": get_user()})


@app.route('/book', methods=['POST'])
def create_book():
    params = request.get_json()
    book = params['book']
    book_id = start_book(book)
    return success_response({"book_id": book_id})

@app.route('/book/<book_id>/<seq>', methods=['GET'])
def book_content(book_id, seq):
    return success_response(get_book_content(book_id, seq))


@app.route('/book/<book_id>/<seq>', methods=['POST'])
def save_user_content_choice(book_id, seq):
    params = request.get_json()
    user_candidate_num = params['candidate_num']
    save_next_book_content(book_id, seq, user_candidate_num)
    return success_response({})

@app.teardown_appcontext
def teardown_db(exception):
    db = g.pop('db', None)

    if db is not None:
        logging.info("Closing database connection")
        db.close()

if __name__ == '__main__':
    # app = create_app()
    CORS(app, resource = {r'*': {"origins": ["https://toy-ai-front.vercel.app/","http://localhost:3000/"]}})

    app.secret_key = get_flask_secret_key()
    app.run(debug=True, host='0.0.0.0', port=8080)