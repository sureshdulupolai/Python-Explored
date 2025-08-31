class Database:
    global_count = 0  # global counter for assigning new IDs

    def __init__(self):
        Database.global_count += 1
        self.count = Database.global_count  # fix count for this instance

    def connect(self):
        return f"Connected to Database : {self.count}"


class Service:
    def __init__(self, db):
        # check if db is instance of Database
        if not isinstance(db, Database):
            raise TypeError(
                "❌ Invalid database object. Use like: db = Database(); service = Service(db)"
            )
        self.db = db

    def get_data(self):
        try:
            return self.db.connect()
        except Exception as e:
            raise RuntimeError("⚠️ Failed to connect with database") from e


# ---- Test ----
db1 = Database()
Service1 = Service(db1)

db2 = Database()
Service2 = Service(db2)

print(Service1.get_data())  # ✅ Connected to Database : 1
print(Service1.get_data())  # ✅ Connected to Database : 1
print(Service2.get_data())  # ✅ Connected to Database : 2

# ❌ This will raise a clear error
Service3 = Service("Suresh")
print(Service3.get_data())
