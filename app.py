from flask import Blueprint
from backend import app
from flask_jwt_extended import JWTManager
from flask_login import LoginManager 
from datetime import datetime
#from flask_cors import CORS
from flask_restplus import Api, Resource
from backend.apimodel import api, api_blueprint
from backend.database import db
from backend.endpoints.client import clientns
from backend.endpoints.pos import posns
from backend.endpoints.auth import authns
from frontend.auth import auth_blueprint
from frontend.main import main_blueprint
import settings

jwt = JWTManager(app)
login_manager = LoginManager()
#cors = CORS(app)
    
def configure_app(flask_app):
    flask_app.config['FLASK_DEBUG'] = settings.FLASK_DEBUG
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SQLALCHEMY_ECHO'] = settings.SQLALCHEMY_ECHO
    flask_app.config['SQLALCHEMY_POOL_RECYCLE'] = settings.SQLALCHEMY_POOL_RECYCLE
    flask_app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
    flask_app.config['SECRET_KEY'] = settings.SECRET_KEY

def initialize_app(flask_app):
    configure_app(flask_app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(flask_app)
    api.init_app(api_blueprint)
    api.add_namespace(clientns)
    api.add_namespace(posns)
    api.add_namespace(authns)
    flask_app.register_blueprint(api_blueprint)
    flask_app.register_blueprint(auth_blueprint)
    flask_app.register_blueprint(main_blueprint)
    db.init_app(flask_app)

    from frontend.models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

def main():
    initialize_app(app)
    app.run(host='0.0.0.0', port=19999)
    #app.run()

if __name__ == "__main__":
    main()