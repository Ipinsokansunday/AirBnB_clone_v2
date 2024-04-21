#!/usr/bin/python3
"""Simple Flask web app with multiple routes."""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    """Returns a simple greeting."""
    return 'Hello HBNB!'

@app.route('/hbnb')
def hello():
    """Returns a message mentioning HBNB."""
    return 'HBNB'

@app.route('/c/<text>')
def c_text(text):
    """Returns 'C' followed by modified text."""
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Returns 'Python' by modified text (default: 'is cool')."""
    return 'Python {}'.format(text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
