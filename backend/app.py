from flask import Flask, request, session

from core.chatGPT.chatGPT import main, book_create

from common.utill.session_user import set_user, get_user
from common.utill.response_type import success_response


app = Flask(__name__)

@app.route('/<user_UUID>', methods=['GET'])
def main_page(user_UUID):
    set_user(user_UUID)
    return success_response({"user": get_user()})

@app.route('/book', methods=['POST'])
def create_book():
    params = request.get_json()
    book = params['book']
    return success_response({"result": book_create(book)})
    

@app.route('/test')
def test():
    msg = main()
    return msg 


if __name__ == '__main__':
    app.secret_key = 'secret-key'
    app.run(debug=True, host='0.0.0.0', port=80)


