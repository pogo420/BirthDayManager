"""
File is essential for routing requests
"""
from flask import Flask, request
from werkzeug.routing import BaseConverter

app = Flask(__name__)


class RegexConverter(BaseConverter):
    """Helper class for regular expression usage"""
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


app.url_map.converters['regex'] = RegexConverter


@app.route("/test", methods=["GET"])
def test():
    """Web portal Test function"""
    return "Test"


@app.route('/get/birthday/<regex("[A-Za-z][A-Za-z0-9]+"):username>/', methods=["GET"])
def get_birthday(username):
    """Function to route birthday request"""
    return f"UserId:{username}"


def delete_birthday():
    """Function to route delete birthday request"""
    pass


def insert_birthday():
    """Function to route insert birthday request"""
    pass

