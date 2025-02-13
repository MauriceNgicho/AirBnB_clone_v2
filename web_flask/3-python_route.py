#!/usr/bin/python3
""" A script that starts a Flask web application """


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Return greetings"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Return greetings """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Return 'C' followed by the text."""
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    """Return 'Python' followed by the text."""
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
