# testing_1.py
import pytest
from Database_File import Database

@pytest.fixture(autouse=True)
def db():
    db = Database(host="localhost", user="root", password="646464", database="testdb")
    yield db
    db.close()

def test_database_connection(db):
    assert db.connected == True

def test_insert_user_and_get(db):
    result = db.insert_user("testuser", "test@example.com", "Test User", False)
    assert result == True
    users = db.get_users()
    assert any(user[1] == "testuser" for user in users)

def test_user_add_data(db):
    result = db.insert_user("john", "john@example.com", "John Doe", True)
    assert result == True

def test_user_duplicate_email(db):
    db.insert_user("alice", "alice@example.com", "Alice", False)
    result = db.insert_user("alice2", "alice@example.com", "Alice2", False)
    assert result == False
