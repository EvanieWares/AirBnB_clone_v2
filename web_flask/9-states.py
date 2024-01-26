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


@app.route('/states/', defaults={'id': ''}, strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id):
    """
    Route /states/ and /states/<id>
    """
    states = storage.all("State").values()
    if id == '':
        states = sorted(states.values(), key=lambda state: state.name)
        return render_template('9-states.html', states=states)
    else:
        id = "State." + id
        state = states[id]
        if state:
            cities = sorted(state.cities, key=lambda city: city.name)
            return render_template(
                '9-states.html',
                state=state,
                cities = cities
                )
    return render_template("9-states.html", not_found=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
