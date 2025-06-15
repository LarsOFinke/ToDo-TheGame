from flask import Blueprint, request, jsonify
from ..db.db_members import add_new_member, get_members_for_team, get_member_count_for_team


members = Blueprint("members", __name__)

    
@members.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    
    if add_new_member(data):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

@members.route('/get-all-members-for-team', methods=['POST'])
def get_all_members_for_team():
    data = request.get_json()

    members: list[dict] = get_members_for_team(data.get('id'))
    return jsonify({"success": True, "members": members}), 200

@members.route('/get-member-count-for-team', methods=['POST'])
def get_total_member_count_for_team():
    data = request.get_json()

    member_count: int = get_member_count_for_team(data.get('id'))
    return jsonify({"success": True, "memberCount": member_count}), 200