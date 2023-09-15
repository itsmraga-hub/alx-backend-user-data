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
def register() -> str:
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


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """
        Implement a login function to respond to the POST /sessions route.
    """
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError:
        abort(400)

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)

    res = jsonify({"email": email, "message": "logged in"})

    response.set_cookie("session_id", session_id)

    return response


@app.route('/sessions', methods=['DELETE'])
def logout() -> str:
    """
        In this task, you will implement a logout function to respond to
        the DELETE /sessions route.
    """
    session_id = request.cookies.get("session_id", None)

    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)

    if user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect('/')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
