#!/usr/bin/python3
"""
Module to develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request
from typing import Dict, Any, List

app = Flask(__name__)

# In-memory dictionary to store users, where each username is associated with a list of user objects
users: Dict[str, List[Dict[str, Any]]] = {}


@app.route("/")
def home():
    """Function to display a welcoming message"""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """Function to get list of all users"""

    # Test if data not in JSON
    if not request.is_json:
        return jsonify({"error": "Request data must be JSON"}), 400

    # Extract only username keys from dict
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

    # Vérification que les données JSON sont valides
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Check if all necessary fields are present
    if "name" not in data or "age" not in data or "city" not in data:
        return jsonify({"error": "All fields (name, age, city) are required"}), 400

    # Check if user with same username and identical data already exists
    if username in users:
        for existing_user in users[username]:
            if (existing_user["name"] == data["name"] and
                existing_user["age"] == data["age"] and
                existing_user["city"] == data["city"]):
                return jsonify({"error": "User with identical data already exists"}), 400

    # Add new user to the list associated with the username
    if username not in users:
        users[username] = []  # Initialize a list for this username if it doesn't exist yet

    users[username].append({
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    })

    # Return new user data + confirm msg
    return jsonify({
        "message": "User added successfully",
        "user": data}), 201

# To run server
if __name__ == "__main__":
    app.run()
