from flask import Flask, request, session

from core.chatGPT.chatGPT import main

from common.utill.session_user import set_user, get_user
from common.utill.response_type import success_response


app = Flask(__name__)

@app.route('/<user_UUID>', methods=['GET'])
def main_page(user_UUID):
    set_user(user_UUID)
    return success_response({"user": get_user()})

# @app.route('/book', methods=['POST'])
# def create_book():
#     get_user()
#     return
    

@app.route('/test')
def test():
    msg = main()
    return msg 


if __name__ == '__main__':
    app.secret_key = 'secret-key'
    app.run(debug=True, host='0.0.0.0', port=80)


