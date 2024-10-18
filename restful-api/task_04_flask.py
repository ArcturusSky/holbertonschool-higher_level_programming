#!/usr/bin/python3
"""
Module to develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire des utilisateurs (déplacé en global pour les routes dynamiques)
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route("/")
def home():
    """Function to display a welcoming message"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Function to get list of all users"""

    # Extract only username key from dict
    usernames = list(users.keys())

    # If no users, return empty list
    return jsonify(usernames)


@app.route("/status")
def status():
    """Function to get current status"""
    return "OK"


@app.route('/users/<username>')
def show_user_profile(username):
    """Function to get a user profile"""
    if username not in users:
        # Return 404 if user not found
        return jsonify({"error": "User not found"}), 404
    # Return user profil object in JSON
    return jsonify(users[username])


# Path to add a user
@app.route("/add_user", methods=["POST"])
def add_user():
    """Function to add a new user via POST request"""
    
    # Extract data sent to the json request
    data = request.get_json()
    username = data.get(username)

    # Check if all fields are given
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if user with same username and identical data already exists
    if username in users:
        existing_user = users[username]
        if (existing_user["name"] == data.get("name") and
            existing_user["age"] == data.get("age") and
            existing_user["city"] == data.get("city")):
            return jsonify({"error": "User with identical data already exists"}), 400

    username = data["username"]

    # Add new user in the global dict `users`
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    # Return new user data + confirm msg
    return jsonify({
        "message": "User added successfully",
        "user": users[username]}), 201


# To run server
if __name__ == "__main__":
    app.run()
