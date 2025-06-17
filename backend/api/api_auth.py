from flask import Blueprint, request, jsonify, session
from ..db.db_auth import validate_user, create_user, get_user_id, update_username, update_password


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if validate_user(username, password):
        session["username"] = username
        user_id = get_user_id(username)
        return jsonify({"success": True, "username": username, "userId": user_id}), 200
    else:
        return jsonify({"success": False}), 401
    
@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    if create_user(data.get("username"), data.get("password")):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401
    
@auth.route("/change-username", methods=["POST"])
def change_username():
    data = request.get_json()
    
    if update_username(data.get("userId"), data.get("newUsername")):
        return jsonify({"success": True, "user": data.get("newUsername")}), 200
    else:
        return jsonify({"success": False}), 401
        
@auth.route("/change-password", methods=["POST"])
def change_password():
    data = request.get_json()
    
    if update_password(data.get("userId"), data.get("newPassword")):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401
    
@auth.route('/clear-session', methods=['GET'])
def clear_session():
    session.clear()  # Clear the session
    
    return jsonify({"success": True}), 200
