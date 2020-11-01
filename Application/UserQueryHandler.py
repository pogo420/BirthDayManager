"""
File is essential for routing requests
"""
from flask import Flask, request
from werkzeug.routing import BaseConverter

from Application.AuthenticationManager import AuthenticationManager
from Application.AuthorizationManager import AuthorizationManager

app = Flask(__name__)


# class RegexConverter(BaseConverter):
#     """Helper class for regular expression usage"""
#     def __init__(self, url_map, *items):
#         super(RegexConverter, self).__init__(url_map)
#         self.regex = items[0]
#
#
# app.url_map.converters['regex'] = RegexConverter


@app.route("/", methods=["GET"])
def test():
    """Web portal Test function"""
    return {"message": "Test Response"}, 201, {'Content-Type': 'application/json'}


@app.route("/authenticate", methods=["GET"])
def authenticate():
    """Web portal Test function"""
    username = request.args.get("username")
    password = request.args.get("password")
    if AuthenticationManager.authenticate(username, password):
        return AuthorizationManager().create_token(username)
    else:
        return


@app.route('/auth/get/birthday/<regex("[A-Za-z][A-Za-z0-9]+"):username>/', methods=["GET"])
def auth_request(username):
    """Function to route birthday request"""
    _, token = request.headers["Authorization"].split()
    if AuthorizationManager().validate_token(username, token):
        return f"UserId:{username}{token}"
    else:
        return "Not Authorized", 403

