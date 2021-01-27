#!/usr/bin/python3
"""Module for Flask REST application."""
from flask import Flask
from models import storage
from api.v1.views import app_views
from os import getenv
from flask import make_response
<<<<<<< HEAD


app = Flask(__name__)
=======
from flask_cors import CORS

# create an instance of the Flask class
app = Flask(__name__)
app.url_map.strict_slashes = False

# create an instance of the CORS class
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

host = getenv('HBNB_API_HOST')
port = getenv('HBNB_API_PORT')

if not host:
    host = "0.0.0.0"

if not port:
    port = 5000

>>>>>>> c712927a3eb858b5430827e26e7931a426c1b57a
app.register_blueprint(app_views)


@app.teardown_appcontext
<<<<<<< HEAD
def closedb(foo):
    """Close db session."""
    storage.close()


if __name__ == "__main__":
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", 5000)
    app.run(host, port, threaded=True)
=======
def remove_session(self):
    """after each request removes the current SQLAlchemy Session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """handler for 404 errors that returns a status code response"""
    return (jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    app.run(host=host, port=port, threaded=True)
>>>>>>> c712927a3eb858b5430827e26e7931a426c1b57a
