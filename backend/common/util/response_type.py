from flask import jsonify, make_response

def success_response(data):
    # data = make_summary()
    return make_response(jsonify(data), 200)