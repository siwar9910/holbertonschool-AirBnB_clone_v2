#!/usr/bin/python3
"""script that starts a Flask web application """
from flask import Flask

# Createing instance of flacks
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_cmsg(text):
    # Printing  msg with specific info
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_pymsg(text="is cool"):
    # Printing msg with specific info
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    """ Initial configuration for fLaks  """
    app.run(host="0.0.0.0", port=5000, debug=True)
