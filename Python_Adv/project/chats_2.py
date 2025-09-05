from chats_1 import Login, logout_required, save_users
from file_decorator import login_required, decorator_already_exist, decorator_gmail, decorator_mobile, decorator_password, admin_only

class Signup(Login):

    ROLE_MAP = {
        "LOGINUSER": "viewer",
        "ADMINUSER": "admin",
        "EDITORUSER": "editor"
    }

    @logout_required
    @decorator_already_exist
    @decorator_gmail
    @decorator_mobile
    @decorator_password
    def __init__(self, mobileno, name, gmail, password, code="LOGINUSER"):
        self.mobile = str(mobileno)
        self.name = name
        self.gmail = gmail
        self.password = password

        # 🔹 Role mapping with .upper()
        role_key = str(code).upper()
        self.cat = Signup.ROLE_MAP.get(role_key, "viewer")   # default viewer

        # Save new user
        new_user = {
            "id" : len(Login.users) + 1,
            "name": self.name,
            "gmail": self.gmail,
            "password": self.password,
            "cat": self.cat,
            "mobile": self.mobile,
        }

        Login.users.append(new_user)

        # Save in file also (sirf ek naya user append karega)
        save_users(new_user)

        # Ab Signup ke baad Login check bhi ho
        super().__init__(mobileno, password)

    def __str__(self):
        # 🔹 Login ka __str__ call kar diya
        return super().__str__()

    @login_required
    def ShowMe(self):
        matches = [f"Name : {i['name']}, Mobile No: {i['mobile']}, Gmail: {i['gmail']}, Category: {i['cat']}" for i in Login.users if self.mobile == i["mobile"] and self.password == i["password"]]
        return matches[0] if matches else None

    @admin_only
    def ShowDetails(self):
        print("🔹 Showing all users:")
        Users = Login.users
        for u in Users:
            print(f"Name: {u['name'].title()}, Gmail: {u['gmail']}, Role: {u['cat']}, Mobile: {u['mobile']}")
        return f"🔹 Finish Detils Record: {len(Users)}"
    
    @admin_only
    def ShowList(self):
        return Login.users

if __name__ == "__main__":
    sg = Signup(name="krish", mobileno=9999999999, gmail='krish@gmail.com', password="suresh@123", code="ADMINUSER")
    print(sg)

    run = ["ShowMe", "ShowDetails", "ShowList"]
    for i in run:
        result = getattr(sg, i)()  # method call
        if result is not None:
            print(result)  # print the return value
        print()

    print("Starting Here: ")
    print()

    # First login
    lg = Login(9820646838, "suresh123")
    print(lg)

    # Try to signup while logged in
    try:
        sg = Signup(9999999999, "krish", "krish@gmail.com", "Suresh@123", "ADMINUSER")
    except PermissionError as e:
        print(e)

    # Logout
    Login.Logout()

    # Now signup will work
    sg = Signup(9999999999, "krish", "krish@gmail.com", "Suresh@123", "ADMINUSER")
    print(sg)