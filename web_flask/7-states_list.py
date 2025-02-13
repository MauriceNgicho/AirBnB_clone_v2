#!/usr/bin/python3
"""Starts a Flask web application to display states"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a HTML page with a list of all State objects"""
    states = storage.all(State).values()  # Fetches all states
    states = sorted(states, key=lambda state: state.name)  # Sort by name
    return render_template('7-states_list.html', states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
