from flask import Blueprint, request, jsonify
from ..crud import add_new_team


teams = Blueprint("teams", __name__)

    
@teams.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    
    if add_new_team(data.get("teamName")):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401
