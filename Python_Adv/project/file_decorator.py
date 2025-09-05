from chats_1 import Login

def decorator_already_exist(init_func):
    def wrapper(self, mobileno: int, name, gmail, password, code="LOGINUSER"):
        mobileno = str(mobileno)

        # Check in existing users
        for user in Login.users:
            if user["gmail"] == gmail:
                raise ValueError("❌ Gmail already exists!")
            if user["mobile"] == mobileno:
                raise ValueError("❌ Mobile number already exists!")

        # Agar unique hai tabhi aage jao
        return init_func(self, mobileno, name, gmail, password, code)
    return wrapper

def decorator_gmail(init_func):
    def wrapper(self, mobileno: int, name, gmail, password, code="LOGINUSER"):
        if not gmail.endswith("@gmail.com"):
            raise ValueError("❌ Invalid Gmail ID. It must end with '@gmail.com'")
        return init_func(self, mobileno, name, gmail, password, code)
    return wrapper

def decorator_mobile(init_func):
    def wrapper(self, mobileno, name, gmail, password, code="LOGINUSER"):
        mobileno = str(mobileno)
        if not (mobileno.isdigit() and len(mobileno) == 10):
            raise ValueError("❌ Invalid Mobile No. It must be 10 digits.")
        return init_func(self, mobileno, name, gmail, password, code)
    return wrapper

def decorator_password(init_func):
    def wrapper(self, mobileno: int, name, gmail, password, code="LOGINUSER"):
        mobileno = str(mobileno)

        # Same check
        if password == name or password == gmail or password == mobileno:
            raise ValueError("❌ Weak Password: Same as name, gmail, or mobile.")

        # Strength check
        if len(password) < 6:
            raise ValueError("❌ Weak Password: Must be at least 6 characters.")
        if not any(ch.isdigit() for ch in password):
            raise ValueError("❌ Weak Password: Must contain at least 1 digit.")
        if not any(ch in "!@#$%^&*_-+=" for ch in password):
            raise ValueError("❌ Weak Password: Must contain at least 1 special character (!@#$%^&*_-+=).")

        return init_func(self, mobileno, name, gmail, password, code)
    return wrapper

def admin_only(func):
    def wrapper(self, *args, **kwargs):
        # Check if user is logged in
        if not Login.log or not self.user:
            raise PermissionError("❌ You must login first to access this function.")

        # Check if user category is admin
        if self.user[0]["cat"].lower() != "admin":
            raise PermissionError("❌ Only admin users can access this function.")

        # All good, call the actual function
        return func(self, *args, **kwargs)
    return wrapper

def login_required(func):
    def wrapper(self, *args, **kwargs):
        if not Login.log or not getattr(self, 'user', None):
            raise PermissionError("❌ You must login first to access this function.")
        return func(self, *args, **kwargs)
    return wrapper


def mobile_validator(func):
    def wrapper(self, mobile, *args, **kwargs):
        mobile_str = str(mobile)

        if len(mobile_str) != 10 or not mobile_str.isdigit():
            raise ValueError("❌ Invalid mobile number. It must be 10 digits only.")

        return func(self, mobile, *args, **kwargs)
    return wrapper