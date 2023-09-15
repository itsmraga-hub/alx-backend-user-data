#!/usr/bin/env python3
"""
    In this task, you will set up a basic Flask app.
"""

from flask import Flask, jsonify, abort, request, redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route("/", methods=['GET'])
def root() -> str:
    """
        root page to respond with jsonified message
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """
        Define a users function that implements the POST /users route.
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    try:
        user = AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
