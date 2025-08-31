class Database:
    def connect(self):
        return "Connected to Database"
    
class Service:
    def __init__(self):
        # it's called hard coding
        # this is code, but in hight level we can connect other database. 
        # we need to use same data base
        self.db = Database() # tight couping

    def get_data(self):
        return self.db.connect()

# Usage
data = Service()
print(data.get_data())