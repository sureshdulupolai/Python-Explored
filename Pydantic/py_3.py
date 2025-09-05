# old style "V1"

# from pydantic import BaseModel, EmailStr, validator

# class User(BaseModel):
#     name: str
#     email: EmailStr
#     account_id: int

#     @validator("account_id")
#     def validate_accound_id(cls, value):
#         if value <= 0:
#             raise ValueError(f"acound_id must be positive: {value}")
#         return value

# # to check a validation email
# user_1 = User(
#     name="Suresh",
#     email="suresh@gamil.com",
#     account_id=1234
# )

# print(user_1)
# print(user_1.name)
# print(user_1.email)
# print(user_1.account_id)

# New Style "V2"
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    email: str
    account_id: int

    @field_validator("account_id")
    @classmethod
    def check_account_id(cls, v):
        if v <= 0:
            raise ValueError("Account ID must be positive")
        return v
    
    # to check if name, and email is not empty
    @field_validator("name", "email")
    @classmethod
    def check_not_empty(cls, v):
        if not v:
            raise ValueError("Field cannot be empty")
        return v


# user = User(name="Suresh", email="suresh@gamil.com", account_id=123)
# print(user)
# print(user.name)
# print(user.email)
# print(user.account_id)


# user = User(name="", email="test@test.com", account_id=1234)
