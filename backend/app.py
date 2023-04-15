from flask import Flask
from core.chatGPT.chatGPT import main

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World!"


@app.route('/test')
def test():
    msg = main()
    return msg 

app.run(debug=True, host='0.0.0.0', port=80)


