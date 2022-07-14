#!/usr/bin/python3
""" starts a Flask web application """
from flask import Flask
# Creating instance of flacks
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_msg(text):
    # printing  msg with specific info
    return 'C %s' % text.replace('_', ' ')


if __name__ == "__main__":
    """ Configure for flasks  """
    app.run(host="0.0.0.0", port=5000, debug=True)
