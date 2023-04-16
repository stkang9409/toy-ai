from flask import jsonify, make_response

def success_response(data, msg="success"):
    return make_response(jsonify({"message": msg, "data": data}), 200)