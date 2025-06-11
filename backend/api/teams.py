from flask import Blueprint, request, jsonify
from ..crud import add_new_team, get_teams_by_user


teams = Blueprint("teams", __name__)

    
@teams.route("/create", methods=["POST"])
def create():
    data = request.get_json()
    
    if add_new_team(data):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401

@teams.route('/get-all-team', methods=['POST'])
def get_all_team():
    data = request.get_json()

    teams: list[dict] = get_teams_by_user(data.get('id'))
    return jsonify({"success": True, "teams": teams}), 200
