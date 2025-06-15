from flask import Blueprint, request, jsonify
from ..db.crud import close_todo, open_todo


todos = Blueprint("todos", __name__)

    
@todos.route("/close", methods=["POST"])
def close():
    data = request.get_json()
    
    if close_todo(data.get("todoId")):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

@todos.route("/open", methods=["POST"])
def open():
    data = request.get_json()
    
    if open_todo(data.get("todoId")):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401
    