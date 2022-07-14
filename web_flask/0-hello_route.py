#!/usr/bin/python3
"""
start a Flask web application:
web application must be listening on 0.0.0.0, port 5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


if __name__ == "__main__":
    """ Init configuration for flaks """
    app.run(host="0.0.0.0", port=5000, debug=True)
