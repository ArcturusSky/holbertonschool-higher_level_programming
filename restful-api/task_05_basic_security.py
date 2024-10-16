#!/usr/bin/python3
"""
Module to develop manage API security and authentication techniques
"""


from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Users listes with hashed passwords
users = {
    "charlie": generate_password_hash("L0v3_V4gG13"),
    "susan": generate_password_hash("0Ld_H4g")
}

# Function to verify if username and if password match with username
@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

# Path protected by the authentication
@app.route("/basic-protected")
@auth.login_required
def welcome():
    return "Basic Auth: Access Granted"


if __name__ == '__main__':
    app.run()