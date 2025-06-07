from flask import Blueprint, request, jsonify
from ..crud import add_new_task, get_all_open_tasks, edit_task, delete_task


tasks = Blueprint("tasks", __name__)
    
    
@tasks.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    
    if add_new_task(data):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

@tasks.route('/get-all-open', methods=['GET'])
def get_all_open():
    tasks: list[dict] = get_all_open_tasks()
    
    return jsonify({"success": True, "tasks": tasks}), 200

@tasks.route("/edit", methods=["POST"])
def edit():
    data = request.get_json()

    if edit_task(data):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

@tasks.route("/delete", methods=["POST"])
def delete():
    data = request.get_json()

    if delete_task(int(data["taskId"])):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

