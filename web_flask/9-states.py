#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import *
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def remove_sqlalchemy_session(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """
    Route /states/ and /states/<id>
    """
    states = storage.all("State")
    if id and id in states:
        return render_template(
            "8-cities_by_states.html",
            state=states[id], state_id=id
            )
    return render_template(
        "8-cities_by_states.html",
        states=states, state_id=id
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
