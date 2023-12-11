from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import path

db = SQLAlchemy()
DB = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'osff-notes-app'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ path.join(app.instance_path, DB)
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_db(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_db(app):
    if not path.exists(path.join(app.instance_path, DB)):
        # Create database models
        with app.app_context():
            db.create_all()
        print('Created Database')
