from flask import jsonify, make_response

def success_response(data, msg="Success"):
    return make_response(jsonify({"message": msg, "data": data}), 200)