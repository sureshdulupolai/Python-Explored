import os
import json
from file_decorator import login_required
from chats_1 import Login

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_FILE = os.path.join(BASE_DIR, "users.json")
FRIENDS_FILE = os.path.join(BASE_DIR, "friends.json")


# ----------------- Helper Functions -----------------
def load_json(file):
    if not os.path.exists(file) or os.path.getsize(file) == 0:
        return []
    with open(file, "r") as f:
        return json.load(f)

def save_json(file, data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

class Friends(Login):

    user_data = load_json(USER_FILE)
    friends_data = load_json(FRIENDS_FILE)
    log = False
    
    def __init__(self, mobile = []):
        if Friends.log:
            self.mobile = mobile
        else:
            print("❌ Login Failed to add frd in chat use: Friends.Login()")

    def __str__(self):
        return "Welcome to chat frd!,.."

    def create_frd(self):
        return {
            "id": len(Friends.friends_data) + 1,
            "userid": 1,
            "friends": [],
            "invite": [],
            "block": []
        }

    def Login(mobile, password):
        u = Login(mobileno=mobile, password=password)
        print(u)
        Friends.log = u.log
        return u

if __name__ == "__main__":
    u = Friends.Login(mobile=9820646838, password="suresh123")
    if u.log and Friends.log:
        # Friends.log = False
        Frd = Friends(mobile=9123456780)
        print("Message: ", Frd)
    else:
        ...