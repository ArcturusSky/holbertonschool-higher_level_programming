#!/usr/bin/python3
"""
Module to develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire des utilisateurs (déplacé en global pour les routes dynamiques)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}

@app.route("/")
def home():
    """Function to display a welcoming message"""
    return "Welcome to the Flask API!"

@app.route("/data")
def get_usernames():
    """Function to get list of all users"""

    # Extraire seulement les clés (usernames) du dictionnaire
    usernames = list(users.keys())
    
    # Retourner la réponse en format JSON
    return jsonify(usernames)

@app.route("/status")
def status():
    """Function to get current status"""
    return "OK"

@app.route('/users/<username>')
def show_user_profile(username):
    """Function to get a user profile"""
    if username not in users:
        return jsonify({"error": "User not found"}), 404  
    # Retourne un code 404 pour utilisateur non trouvé
    
    return jsonify(users[username])  # Retourne l'objet utilisateur en JSON

# Route pour ajouter un utilisateur via une requête POST
@app.route("/add_user", methods=["POST"])
def add_user():
    """Function to add a new user via POST request"""
    # Extraire les données JSON envoyées dans la requête
    data = request.get_json()

    # Vérifier que toutes les informations nécessaires sont présentes
    if not data or "username" not in data:
        return jsonify({"error": "Invalid data"}), 400

    username = data["username"]

    # Ajouter l'utilisateur dans le dictionnaire global `users`
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }

    # Retourner un message de confirmation avec les données de l'utilisateur ajouté
    return jsonify({"message": "User added successfully", "user": users[username]}), 201

# Pour lancer le serveur
if __name__ == "__main__":
    app.run()