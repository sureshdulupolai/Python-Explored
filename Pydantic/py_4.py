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

# user_json = user_1.json()
# print(user_json) # v1

# v2
user_json = user_1.model_dump_json()
print(user_json)

# user_json_dict = user_1.dict()
# print(user_json_dict) # v1

# V2
user_json_dict = user_1.model_dump()
print(user_json_dict)


json_str = '{"name":"Suresh","email":"suresh@gmail.com","account_id":1234}'
user_2 = User.model_validate_json(json_str)
print(user_2.name)
