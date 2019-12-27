from flask import Flask, Blueprint
from flask_jwt_extended import JWTManager
from datetime import datetime
from flask_restplus import Api, Resource
from backend.apimodel import api
from backend.database import db
from backend.endpoints.client import clientns
from backend.endpoints.pos import posns
from backend.endpoints.auth import authns
import settings

app = Flask(__name__)
jwt = JWTManager(app)

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SQLALCHEMY_ECHO'] = settings.SQLALCHEMY_ECHO
    flask_app.config['SQLALCHEMY_POOL_RECYCLE'] = settings.SQLALCHEMY_POOL_RECYCLE
    flask_app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY

def initialize_app(flask_app):
    configure_app(flask_app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(clientns)
    api.add_namespace(posns)
    api.add_namespace(authns)
    flask_app.register_blueprint(blueprint)
    db.init_app(flask_app)

def main():
    initialize_app(app)
    app.run(debug=True)

if __name__ == "__main__":
    main()