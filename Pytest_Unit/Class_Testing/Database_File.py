# database.py
import mysql.connector

class Database:
    def __init__(self, host="localhost", user="root", password="", database="testdb"):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conn.cursor()
            self.connected = True
        except Exception as e:
            print(f"❌ Database connection failed: {e}")
            self.connected = False

    def insert_user(self, username, email, fullname, admin=False):
        try:
            sql = "INSERT INTO users (username, email, fullname, admin) VALUES (%s, %s, %s, %s)"
            values = (username, email, fullname, admin)
            self.cursor.execute(sql, values)
            self.conn.commit()
            return True
        except Exception as e:
            print(f"❌ Error inserting user: {e}")
            return False

    def get_users(self):
        try:
            self.cursor.execute("SELECT * FROM users")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"❌ Error fetching users: {e}")
            return []

    def close(self):
        if self.connected:
            self.cursor.close()
            self.conn.close()
            self.connected = False
