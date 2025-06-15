from flask import Blueprint, request, jsonify
from ..db.crud import add_new_member, get_members_by_team


members = Blueprint("members", __name__)

    
@members.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    
    if add_new_member(data):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

@members.route('/get-all-members', methods=['POST'])
def get_all_members():
    data = request.get_json()

    members: list[dict] = get_members_by_team(data.get('id'))
    return jsonify({"success": True, "members": members}), 200
