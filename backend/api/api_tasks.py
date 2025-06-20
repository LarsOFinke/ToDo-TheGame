from flask import Blueprint, request, jsonify
from ..db.db_tasks import add_new_task, get_all_open_tasks_user, get_all_open_tasks_team, get_done_tasks_count, edit_task, delete_task, close_task


tasks = Blueprint("tasks", __name__)
    
    
@tasks.route("/add", methods=["POST"])
def add():
    data = request.get_json()

    if add_new_task(data.get("mode"), data):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

@tasks.route('/get-all-open-user', methods=['POST'])
def get_all_open_user():
    data = request.get_json()

    tasks: list[dict] = get_all_open_tasks_user(data.get('id'))
    return jsonify({"success": True, "tasks": tasks}), 200

@tasks.route('/get-all-open-team', methods=['POST'])
def get_all_open_team():
    data = request.get_json()

    tasks: list[dict] = get_all_open_tasks_team(data.get('id'))
    return jsonify({"success": True, "tasks": tasks}), 200

@tasks.route('/get-done-count', methods=['POST'])
def get_done_count():
    data = request.get_json()

    done_count: list[dict] = get_done_tasks_count(data.get('userId'))
    return jsonify({"success": True, "doneCount": done_count}), 200


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

@tasks.route("/close", methods=["POST"])
def close():
    data = request.get_json()

    if close_task(int(data["taskId"])):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401
