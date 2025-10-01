from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # ✅ __repr__ / __str__ jaisa
    def __repr__(self):
        return f"<User {self.username}>"

    # ✅ Custom function (instance method)
    def full_info(self):
        return f"User: {self.username}, Email: {self.email}"

    # ✅ Save jaisa method (Django ke save() ka alternate)
    def save(self):
        db.session.add(self)
        db.session.commit()

    # ✅ Delete method
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # ✅ Class method (filtering ke liye)
    @classmethod
    def get_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    # ✅ Static method (koi DB kaam nahi, sirf utility)
    @staticmethod
    def is_valid_username(username):
        return len(username) >= 3


# New user banao
u1 = User(username="suresh", email="suresh@example.com")
u1.save()  # direct save()

# __repr__ / __str__ use hoga
print(u1)   # <User suresh>

# Custom function call
print(u1.full_info())  
# Output: User: suresh, Email: suresh@example.com

# Delete user
# u1.delete()

# Class method use karke filter
user = User.get_by_email("suresh@example.com")
print(user.username)  # suresh

# Static method test
print(User.is_valid_username("ab"))   # False
print(User.is_valid_username("suresh"))  # True


# 🔹 Django vs Flask Comparison

# | Django (ORM)                | Flask-SQLAlchemy (ORM)       |
# | --------------------------- | ---------------------------- |
# | `__str__`                   | `__repr__` ya apna method    |
# | `save()`                    | khud likho `save()` method   |
# | `delete()`                  | khud likho `delete()` method |
# | Custom instance methods     | Same syntax                  |
# | `@classmethod` (filters)    | Same syntax with `cls.query` |
# | `@staticmethod` (utilities) | Same syntax                  |
