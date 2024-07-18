#!/usr/bin/env python3
"""
Flask app to handle authentication routes
"""
from flask import Flask, jsonify, request, abort, redirect, url_for
from auth import Auth

app = Flask(__name__)
auth = Auth()


@app.route('/sessions', methods=['POST'])
def login():
    """Log in a user."""
    email = request.form.get('email')
    password = request.form.get('password')
    if email is None or password is None:
        abort(401)
    if not auth.valid_login(email, password):
        abort(401)
    session_id = auth.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """Log out a user."""
    session_id = request.cookies.get('session_id')
    if session_id is None:
        abort(403)
    user = auth.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    auth.destroy_session(user.id)
    return redirect(url_for('index'))


@app.route('/', methods=['GET'])
def index():
    """Index route."""
    return jsonify({"message": "Welcome to the authentication system"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
