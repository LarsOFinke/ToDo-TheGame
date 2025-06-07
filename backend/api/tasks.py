from flask import Blueprint, request, jsonify
from ..crud import add_new_task


tasks = Blueprint("tasks", __name__)
    
    
@tasks.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    
    if add_new_task(data):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401



@tasks.route("/edit", methods=["POST"])
def edit():
    data = request.get_json()
    print(data)
    return jsonify({"success": True}), 200
    if add_new_task(data):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401


# @tasks.route('/clear-session', methods=['GET'])
# def clear_session():
#     session.clear()  # Clear the session
    
#     return jsonify({"success": True}), 200
