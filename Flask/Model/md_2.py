from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# ✅ BaseModel: sabke liye common fields
class BaseModel(db.Model):
    __abstract__ = True  # iska apna table nahi banega

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

# ✅ User Model
class User(BaseModel):
    __tablename__ = "users"

    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(
        db.Enum("admin", "editor", "viewer", name="user_roles"),
        default="viewer",
        nullable=False,
    )

    profile = db.relationship("Profile", backref="user", uselist=False)

    def __repr__(self):
        return f"<User {self.username}>"

# ✅ Profile Model (User se linked)
class Profile(BaseModel):
    __tablename__ = "profiles"

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    bio = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Profile of {self.user.username}>"


# 🔹 Breakdown (line by line explanation without field detail)
# db = SQLAlchemy() → Flask ke liye database ORM initialise ho raha hai.
# BaseModel → ek abstract class banayi gayi hai jisme common columns (id, created_at, updated_at) rakhe gaye hain. Iska apna table DB me nahi banega.
# User class → BaseModel se inherit karke ek users table create karega jisme user ka data (username, email, role) store hoga.
# profile relationship banayi gayi hai taaki ek user ka ek hi profile ho (one-to-one relation).
# Profile class → BaseModel se inherit karke ek profiles table banata hai jo user_id ke through users table se connected hai.
# __repr__ methods → debugging aur readability ke liye custom string return karte hain (jaise <User suresh>).

# 👉 Overall, is code me tumne inheritance + one-to-one relationship implement kiya hai.
# User aur Profile dono tables apne-apne data hold karte hain.
# Har User ka ek hi Profile ho sakta hai.
# BaseModel ensure karta hai ki dono tables me id, created_at, aur updated_at automatically rahe.