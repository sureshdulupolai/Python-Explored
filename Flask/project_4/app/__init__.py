from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.__init__(app) # db se apna app link karna

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp

    app.register_blueprint(auth_bp, url_prefix="/auth") # related routes in particular app
    app.register_blueprint(tasks_bp, url_prefix="/tasks")

    with app.app_context():
        db.create_all()

    return app