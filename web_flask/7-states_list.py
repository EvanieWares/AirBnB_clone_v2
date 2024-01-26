#!/usr/bin/python3
"""A script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def remove_sqlalchemy_session(exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Route /states_list
    Displays a HTML page
        - 'H1' tag: "States"
        - 'UL' tag: with the list of all 'State' objects present in DBStorage
          sorted by name (A->Z)
            - 'LI' tag: description of one 'State': <state.id>: <B><state.name>
              </B> + 'UL' tag: with the list of 'City' objects linked to the
              'State' sorted by name (A->Z)
                - 'LI' tag: description of one 'City': <city.id>:
                  <B><city.name></B>
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
