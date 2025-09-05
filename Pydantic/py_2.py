# pip install pydantic[email]
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

# to check a validation email
user_1 = User(
    name="Suresh",
    email="suresh",
    account_id=1234
)

print(user_1)
print(user_1.name)
print(user_1.email)
print(user_1.account_id)
