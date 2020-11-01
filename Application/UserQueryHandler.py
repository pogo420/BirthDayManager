"""
File is essential for routing requests
"""

from flask import Flask, request
from werkzeug.routing import BaseConverter
from Application.AuthenticationManager import AuthenticationManager
from Application.AuthorizationManager import AuthorizationManager
from Application.UserQueryTranslator import UserQueryTranslator

app = Flask(__name__)


# for regex in url
class RegexConverter(BaseConverter):
    """Helper class for regular expression usage"""
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route("/", methods=["GET"])
def test():
    """End point for test response"""
    return "Test Response", 201


@app.route("/authenticate", methods=["GET"])
def authenticate():
    """End point for authentication"""
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if AuthenticationManager().authenticate(username, password):
        return AuthorizationManager().create_token(username), 201
    else:
        return "Authentication Failed", 403


@app.route('/auth/<regex("[A-Za-z][A-Za-z0-9]+"):username>/process-data', methods=["GET"])
def process_data(username):
    """End point for processing data"""
    _, token = request.headers["Authorization"].split()
    if AuthorizationManager().validate_token(username, token):
        if request.json:
            return UserQueryTranslator(request.json).process_data()
        else:
            return "No Payload", 403
    else:
        return "Not Authorized", 403
