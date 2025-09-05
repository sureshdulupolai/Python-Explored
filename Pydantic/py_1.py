from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int

user_1 = User(
    name="Suresh",
    email="suresh@gmail.com",
    account_id=1234
)
print(user_1)
print(user_1.name)
print(user_1.email)
print(user_1.account_id)

# 
print()

user_data = {
    "name" : "Pritam",
    "email" : "pritam@gmail.com",
    "account_id" : 1235
}
user_2 = User(**user_data)
print(user_2.name)
print(user_2.email)
print(user_2.account_id)


# Data Validation -> Show Error Earliy To Debug Better In Pydantic 
# if you pass digit in string formate it work, but you enter some character then is will show an error
user_3 = User(name="Suresh", email="suresh@gmail.com", account_id="hello")
print(user_3)