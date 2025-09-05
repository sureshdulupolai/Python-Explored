from datetime import datetime

class User:
    def __init__(self, db, username, email, full_name, admin=False):
        self.db = db
        self.username = username
        self.email = email
        self.full_name = full_name
        self.admin = admin
        self.len = self.db.get_next_id("users")  # assume tumne function banaya hai

    def create_dict(self):
        return {
            "id": self.len,
            "username": self.username,
            "email": self.email,   # ✅ FIXED
            "full_name": self.full_name,
            "admin": int(self.admin),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    def add_data(self):
        data = self.create_dict()
        self.db.insert("users", data)
        return data
