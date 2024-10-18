#!/usr/bin/python3
"""Module compiled with Python3"""


from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Function that handles index"""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    Function that converts in JSON and returns the keys of the users dictionary
    """
    users_keys = list(users.keys())
    return jsonify(users_keys)


@app.route('/users/<username>')
def user_data(username):
    """Function that handles the users data"""
    user_data = users.get(username)
    if not user_data:
        return jsonify({"error": "User not found"}), 404
    else:
        return jsonify(user_data)


@app.route('/add_user', methods=['POST'])
def add_user():
    """Function that allows the addition of new users"""
    new_user = request.get_json()
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


@app.route('/status')
def status():
    """Returns the status of the server"""
    return "OK"


if __name__ == "__main__":
    app.run()