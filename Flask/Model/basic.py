db = 1

# start
# -------------------------------------------------------------------------------
# 🔹 Field (Column) Types

# String (varchar jaisa, max length dena optional hai)
db.String(50)      

# Integer (number, auto increment ya normal integer)
db.Integer         

# Float (decimal values)
db.Float           

# Boolean (True/False)
db.Boolean         

# Date & Time
db.Date             # sirf date
db.Time             # sirf time
db.DateTime         # date + time

# Text (long text / description, koi limit nahi)
db.Text             

# Large Binary (images, files, etc.)
db.LargeBinary      

# Enum (choices/limited set of values)
db.Enum("admin", "editor", "viewer", name="user_roles")

# JSON (Postgres ya modern DB me use hota hai)
db.JSON


from datetime import datetime, date, time
# -------------------------------------------------------------------------------
# 🔹 Common Field Parameters (Options)

db.Column(db.String(50),
    primary_key=True,   # Is column ko primary key banata hai
    autoincrement=True, # Auto increment karega (sirf numbers par kaam karta hai)
    unique=True,        # Duplicate values allow nahi hongi
    nullable=False,     # Required field (empty nahi ho sakta)
    nullable=True,      # Optional field (empty ho sakta hai)
    default="viewer",   # Default value (agar user ne kuch nahi diya)
    index=True,         # Faster searching ke liye index banata hai
    onupdate=datetime.utcnow,  # Record update hone par auto update value
)


# -------------------------------------------------------------------------------
# 🔹 Example with All Options

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # PK with auto increment
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)  # unique & required
    email = db.Column(db.String(120), unique=True, nullable=False)   # email must be unique
    bio = db.Column(db.Text, nullable=True)                          # optional long text
    is_active = db.Column(db.Boolean, default=True, nullable=False)  # boolean with default
    role = db.Column(db.Enum("admin", "editor", "viewer", name="roles"), default="viewer")
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)  # auto timestamp
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
