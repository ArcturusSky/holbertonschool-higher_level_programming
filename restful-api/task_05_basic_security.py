#!/usr/bin/python3
"""
Module to develop manage API security and authentication techniques
"""


JWT_SECRET_KEY = "Ch4Gg13" # Constant for clearer code

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
    verify_jwt_in_request,
    get_jwt,
)
from functools import wraps

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY # secure key
jwt = JWTManager(app)


# Users list with hashed passwords
users = {
    "charlie": {
        "username": "Charlie",
        "password": generate_password_hash("L0v3_V4gG13"),
        "role": "admin",
    },
    "susan": {
        "username": "Susan",
        "password": generate_password_hash("0Ld_H4g"),
        "role": "user",
    },
}


# Function to verify if username and if password match with username
@auth.verify_password
def verify_password(username, password):
    """Verify username and password match."""
    if username in users and \
            check_password_hash(users[username]["password"], password):
        return username


# Path protected by the authentication
@app.route("/basic-protected")
@auth.login_required
def welcome():
    """Protected route that returns a welcome message."""
    return jsonify({"Basic Auth: Access Granted"}), 200


# Custom decorator created to verify if request is JWT
# and if user is an admin. Seen in flask.jwt-extended doc
def admin_required():
    """Decorator to check if user is an admin."""
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if claims["is_admin"]:
                # Note: this below means "any function with any arg and any keywords"
                return fn(*args, **kwargs)
            else:
                return jsonify({"error":"Admin access required"}), 403
        return decorator
    return wrapper


# Path protected by JWT with payload, I think.
@app.route("/login", methods=["POST"])
@auth.login_required
def login():
    """Authenticate user and return a JWT token."""
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    # Check if all requiered filed are given. If not 400 Bad request
    if not username or not password:
         return jsonify({"msg": "Missing username or password"}), 400

    # Check authentication, if not 401 Unauthorized
    if username not in users or \
            not check_password_hash(users[username]["password"], password):
            return jsonify({"msg": "Invalid credentials"}), 401

    # Generate and return JWT
    else:
        # Retrieve the user's role
        user_role = users[username]["role"]

        # If admin, get admin acces
        if user_role == "admin":
            access_token = create_access_token(identity=username,
             additional_claims={"is_admin": True})
            return jsonify(access_token=access_token), 200
    
        # If not admin, regular access
        else:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token), 200


# Path proctected by simple JWT, I think.
@app.route("/jwt-protected", methods=["GET"])
@jwt_required
def protected():
    """Protected route that returns the current user's identity."""
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

# Path for admin only
@app.route("/admin-only", methods=["GET"])
@admin_required()
def only_admin_access():
    """Protected route that only admin can access."""
    return jsonify({"Admin Access":"Access Granted"})

# Handling errors
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ == '__main__':
    app.run()
