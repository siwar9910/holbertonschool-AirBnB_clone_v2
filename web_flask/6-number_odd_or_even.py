#!/usr/bin/python3
"""start a Flask web application """
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def print_cmsg(text):
    # printing msg with specific info
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_pymsg(text="is cool"):
    # printing msg with specific info
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def print_number(n):
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ returning a template at the /number_template/<n> route """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    """ Returning a template at the /number_odd_or_even/<int:n> route """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    """ Initial configuration for flaks  """
    app.run(host="0.0.0.0", port=5000, debug=True)
