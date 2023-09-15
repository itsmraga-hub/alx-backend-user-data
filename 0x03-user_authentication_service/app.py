#!/usr/bin/env python3
"""
    In this task, you will set up a basic Flask app.
"""

from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/", methods=['GET'])
def root() -> str:
    """
        root page to respond with jsonified message
    """
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
