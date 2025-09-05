def logout_required(func):
    def wrapper(self, *args, **kwargs):
        if Login.log:
            raise PermissionError("❌ Please logout before creating a new user or logging in again.")
        return func(self, *args, **kwargs)
    return wrapper

import os
import json

# ✅ Always point to the project folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))   # yeh file ka directory lega
USER_FILE = os.path.join(BASE_DIR, "users.json")       # project/users.json

def load_users():
    if os.path.exists(USER_FILE) and os.path.getsize(USER_FILE) > 0:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return []

def save_users(user):
    users = load_users()
    users.append(user)
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

class Login:

    users = load_users()
    log = False
    Uid = None

    @logout_required
    def __init__(self, mobileno, password):
        self.mobile = str(mobileno)  # int ko string bana diya
        self.password = password
        self.user = self.LogUser()

    @logout_required
    def LogUser(self):
        return [i if i else 0 for i in Login.users if i["mobile"] == self.mobile and i["password"] == self.password]

    def __str__(self):
        if self.user:
            Login.log = True
            Login.Uid = self.user[0]['id']
            return f"✅ Login Successful '{self.user[0]['name'].title()}' in Chat App in Python"
        else:
            return "❌ Invalid Mobile or Password"

if __name__ == "__main__":
    lg = Login(mobileno=9820646838, password="suresh123")
    print(lg.log)
    print(lg)
    print(lg.log)
