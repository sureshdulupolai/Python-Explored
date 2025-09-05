# pydantic vs dataclasses 

from dataclasses import dataclass

@dataclass
class User:
    name: str
    email: str
    account_id: int

user = User(name="Suresh", email="suresh@gmail.com", account_id="1234")
print(user)

#

from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    account_id: int

user = User(name="Suresh", email="suresh@gmail.com", account_id="1234")
print(user)

"""

| Feature                                                   | Dataclasses ✅                    | Pydantic ✅                              |
| --------------------------------------------------------- | -------------------------------- | --------------------------------------- |
| Auto `__init__`, `__repr__`                               | ✔️                               | ✔️                                      |
| Type checking                                             | ❌ (runtime pe ignore hota hai)   | ✔️ (strict or smart parsing)            |
| Validation                                                | ❌ (tumhe manually likhna padega) | ✔️ Built-in (validators, constraints)   |
| Default values                                            | ✔️                               | ✔️                                      |
| Nested models                                             | ❌ (manually handle)              | ✔️ Easy (auto parsing of nested dicts)  |
| Performance                                               | ⚡ Fast (lightweight)             | Thoda slow (kyunki validation hoti hai) |
| Extra features (JSON export, ORM mode, env parsing, etc.) | ❌                                | ✔️ Rich support                         |


"""