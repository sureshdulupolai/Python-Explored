# class FamilyMember:
#     def __init__(self, name):
#         self.name = name
    
#     def introduce(self):
#         return f"I am {self.name}"
    

# fm1 = FamilyMember("Suresh")
# fm1 = FamilyMember("Suresh")
# fm1 = FamilyMember("Suresh")
# print(fm1.introduce())

# SingleTen
from abc import ABC, abstractmethod

class FamilyMember(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def introduce(self):
        pass

class FatherMember(FamilyMember):
    _instance = None

    def __new__(cls, name):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        else:
            cls._instance

    def __init__(self, name):
        if not hasattr(self, "initialized"):
            super().__init__(name)
            self.initialized = True

class KidMember(FamilyMember):
    def introduce(self):
        return f"I am {self.name}"
    
km1 = KidMember("Sonu")
km2 = KidMember("Monu")
print(km1.introduce())
print(km2.introduce())

fm1 = FamilyMember("Suresh")
fm2 = FatherMember("Ramesh")
print(fm1.introduce())
print(fm2.introude())