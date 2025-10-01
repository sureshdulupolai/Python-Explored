from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"  # Table ka naam explicitly dena best practice hai

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # Required fields
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Optional field (null allowed)
    phone = db.Column(db.String(15), nullable=True)

    # Boolean with default value
    is_active = db.Column(db.Boolean, default=True, nullable=False)

    # Choice field jaisa (enum use karte hain)
    role = db.Column(
        db.Enum("admin", "editor", "viewer", name="user_roles"),
        default="viewer",
        nullable=False
    )

    # Created & Updated timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.username}>"
