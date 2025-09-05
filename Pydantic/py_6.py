# Auto __init__, __repr__
from dataclasses import dataclass

@dataclass
class UserDC:
    name: str
    age: int

u = UserDC("Suresh", 25)
print(u)   # Auto __repr__


from pydantic import BaseModel

class UserPD(BaseModel):
    name: str
    age: int

u = UserPD(name="Suresh", age=25)
print(u)   # Auto __repr__


# --------------------------------------------------------------------------------
# Type Checking
u = UserDC("Suresh", "25")   # ❌ string diya
print(u)   # Accept kar lega, koi error nahi

u = UserPD(name="Suresh", age="25")  # string diya
print(u)   # ✔️ Auto convert karega int me


# --------------------------------------------------------------------------------
# Validation
@dataclass
class ProductDC: # manually
    name: str
    price: float

    def __post_init__(self):
        if self.price <= 0:
            raise ValueError("Price must be positive")

p = ProductDC("Pen", -10)  # ❌ Error


from pydantic import field_validator

class ProductPD(BaseModel): # build in
    name: str
    price: float

    @field_validator("price")
    @classmethod
    def check_price(cls, v):
        if v <= 0:
            raise ValueError("Price must be positive")
        return v

p = ProductPD(name="Pen", price=-10)  # ❌ Error


# --------------------------------------------------------------------------------
# Default Value
@dataclass
class ConfigDC:
    debug: bool = True

print(ConfigDC())  # debug=True

class ConfigPD(BaseModel):
    debug: bool = True

print(ConfigPD())  # debug=True
# 👉 Dono me kaam karta hai.


# --------------------------------------------------------------------------------
# Nested Models

@dataclass
class AddressDC:
    city: str
    pin: int

@dataclass
class UserWithAddrDC:
    name: str
    address: AddressDC

addr = {"city": "Mumbai", "pin": 400001}
# ❌ Dataclass me tumhe manually convert karna hoga
user = UserWithAddrDC("Suresh", AddressDC(**addr))
print(user)


class AddressPD(BaseModel): # primary key
    city: str
    pin: int

class UserWithAddrPD(BaseModel):
    name: str
    address: AddressPD # foregin key

addr = {"city": "Mumbai", "pin": 400001}
# ✔️ Dict se bhi direct chalega
user = UserWithAddrPD(name="Suresh", address=addr)
print(user)


# --------------------------------------------------------------------------------
# Performance

import time

# Dataclass
start = time.time()
for _ in range(100000):
    UserDC("Suresh", 25)
print("Dataclass:", time.time() - start)

# Pydantic
start = time.time()
for _ in range(100000):
    UserPD(name="Suresh", age=25)
print("Pydantic:", time.time() - start)


# --------------------------------------------------------------------------------
# Extra Features (JSON export)
import json
user = UserDC("Suresh", 25)
print(json.dumps(user.__dict__))  # manually convert


user = UserPD(name="Suresh", age=25)
print(user.model_dump_json())  # direct JSON export
