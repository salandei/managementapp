from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'osff-notes-app'
    app.config['SQLALCHEMY_DATABASE_URL'] = f'sqlite:///{DB}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_db(app)

    return app

def create_db(app):
    if not path.exists(f'notesapp/{DB}'):
        # Create database models
        db.create_all(app=app)
        print('Created Database')
