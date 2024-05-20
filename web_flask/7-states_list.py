#!/usr/bin/python3
""" Start a Flask web application to list states from the database."""

 from flask import Flask, render_template
 from models import storage
 from models.state import State

 app = Flask(__name__)
 app.url_map.strict_slashes = False

 @app.route('/states_list', strict_slashes=False)
 def states_list():
     """Display a HTML page with a list of states"""
     states = sorted(storage.all(State).values(), key=lambda state: state.name)
     return render_template('7-states_list.html', states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
