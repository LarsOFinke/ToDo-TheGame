from flask import Blueprint, request, jsonify, session, redirect, url_for
from ..crud import validate_user, create_user


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get('username')
    
    if validate_user(username, data.get('password')):
        session["username"] = username
        if username == "admin":
            session["is_admin"] = True
            
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401
    
    
@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    if create_user(data.get("username"), data.get("password")):
        return jsonify({"success": True}), 200
    else:
        return jsonify({"success": False}), 401


@auth.route('/clear-session', methods=['GET'])
def clear_session():
    session.clear()  # Clear the session
    
    return jsonify({"success": True}), 200
