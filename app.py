"""
This file have the server restapi.
For run the restapi execute the file 'index.py'.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.clothes import restapi_routes
from helpers.config import CONFIG

# creating
restapi = Flask(__name__)

# settings
restapi.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{CONFIG['SQLITE_DB_PATH']}"
restapi.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# using database
SQLAlchemy(restapi)

# using routes
restapi.register_blueprint(restapi_routes)
