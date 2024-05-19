#!/usr/bin/python3
""" Script to start a Flask web application with 3 view functions """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_world():
    """ Returns some text for the root route """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello():
    """ Returns some text for the /hbnb route """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Returns 'C ' followed by the value of the text variable with underscores replaced by spaces """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

