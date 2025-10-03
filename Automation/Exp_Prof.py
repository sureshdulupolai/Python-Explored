# =============================================
# Full Examples for Search & History Classes
# =============================================

# ---------------------------- Imports ----------------------------
from typing import List, Dict, Any, Union, Optional
from Search import Search, History
# (Assume Search, History classes are already defined here or imported)

# ---------------------------- Search Class Examples ----------------------------

# 1️⃣ String list, lowercase (default Lw=True)
s1 = Search(MainList=["Andheri", "Versova"])
print(s1.list)
# Output: ['andheri', 'versova']
print(s1.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# 2️⃣ String list, no lowercase (Lw=False)
s2 = Search(MainList=["Andheri", "Versova"], Lw=False)
print(s2.list)
# Output: ['Andheri', 'Versova']
print(s2.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# 3️⃣ String tuple
s3 = Search(MainList=("Sakinaka", "Marol Naka"))
print(s3.list)
# Output: ['sakinaka', 'marol naka']
print(s3.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# 4️⃣ String set
s4 = Search(MainList={"Ghatkopar", "Andheri"})
print(s4.list)
# Output: ['ghatkopar', 'andheri']  # order may vary due to set
print(s4.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# 5️⃣ Dict list with Key
s5 = Search(MainList=[{"name": "Andheri"}, {"name": "Versova"}], Key="name")
print(s5.list)
# Output: ['andheri', 'versova']
print(s5.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# 6️⃣ Dict list missing Key
s6 = Search(MainList=[{"place": "Versova"}], Key="name")
print(s6.list)
# Output: []
print(s6.init_error)
# Output: {'status': False, 'details': "Key 'name' not found in dict {'place': 'Versova'}", 'Project-Name': 'my_project'}

# 7️⃣ Dict list with empty dict
s7 = Search(MainList=[{}], Key="name")
print(s7.list)
# Output: []
print(s7.init_error)
# Output: {'status': False, 'details': 'Dict inside MainList cannot be empty', 'Project-Name': 'my_project'}

# 8️⃣ Mixed types (string + dict)
s8 = Search(MainList=["Andheri", {"name": "Versova"}])
print(s8.list)
# Output: []
print(s8.init_error)
# Output: {'status': False, 'details': 'All elements must be of same type as first element', 'Project-Name': 'my_project'}

# 9️⃣ Invalid first element type (non-string/dict)
s9 = Search(MainList=[123, 456])
print(s9.list)
# Output: []
print(s9.init_error)
# Output: {'status': False, 'details': 'Elements must be string or dict', 'Project-Name': 'my_project'}

# 10️⃣ Empty list
s10 = Search(MainList=[])
print(s10.list)
# Output: []
print(s10.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# 11️⃣ MainList is None
s11 = Search()
print(s11.list)
# Output: []
print(s11.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# 12️⃣ Appending new data to existing project
s12 = Search(MainList=["Marol"], ProjectName="my_project")
print(s12.list)
# Output: ['andheri', 'versova', 'marol']  # previously created list is appended

# 13️⃣ Single search (substring or prefix)
result = s1.single_search("And")
print(result)
# Output: {'search': ['andheri'], 'find': 1, 'count': 1}

# 14️⃣ Show all projects
print(Search.show_all_projects())
# Output: [{'Project-Name': 'my_project', 'details': ['andheri', 'versova', 'marol']}]

# ---------------------------- Dict Choice Examples ----------------------------
data = {
    "students": [
        {"name": "Suresh", "scores": (95, 88, 76)},
        {"name": "Ravi", "scores": (78, 85, 82)}
    ],
    "class": "Python Basics",
    "topics": ["dict", "list", "tuple"],
    "meta": {"year": 2025, "active": True},
    "misc": {"sets": {1, 2, 3}}
}

# Nested tuple → convert to string
print(Search.dict_choice(data, Keys="students.scores"))
# ['95','88','76','78','85','82']

# Single string value
print(Search.dict_choice(data, Keys="class"))
# ['Python Basics']

# List of strings
print(Search.dict_choice(data, Keys="topics"))
# ['dict','list','tuple']

# Integer/boolean → convert to string
print(Search.dict_choice(data, Keys="meta.year"))
# ['2025']
print(Search.dict_choice(data, Keys="meta.active"))
# ['True']

# Set → convert to string
print(Search.dict_choice(data, Keys="misc.sets"))
# ['1','2','3']  # order may vary

# Multiple Keys
print(Search.dict_choice(data, Keys=["class", "students.scores"]))
# ['Python Basics','95','88','76','78','85','82']

# Using repeat=True to remove duplicates
data2 = [data, data]
print(Search.dict_choice(data2, Keys=["class","students.scores"], repeat=True))
# ['Python Basics','95','88','76','78','85','82']

# Strict type check
print(Search.dict_choice(data, Keys=["students.scores"], str_type=False))
# {'error': 'Non-string value found: 95', 'status': 'fail'}

# Error case
print(Search.dict_choice(data, Keys=["students.age"]))
# {'error': "Key path 'students.age' not found in dict {...}", 'status': 'fail'}

# ---------------------------- History Class Examples ----------------------------
history_data = ["Login", "Search: Python", "Open File", "Run Script", "Logout"]
hist = History(history_data)

# Full history
print(hist.all())
# ['Logout', 'Run Script', 'Open File', 'Search: Python', 'Login']

# Navigation
print(hist.next())     # 'Logout'
print(hist.next())     # 'Run Script'
print(hist.previous()) # 'Logout'

# First, last, middle
print(hist.first())  # 'Login'
print(hist.last())   # 'Logout'
print(hist.middle()) # 'Open File'

# Index continues
print(hist.next())  # 'Run Script'

# ---------------------------- CSV Examples ----------------------------
def TestingCSV():
    my_filter = Search()
    path = "employees.csv"  # CSV file with appropriate format

    # Get simple column
    print(my_filter.from_csv(path, Keys=["name"]))
    # ['Amit', 'Neha']

    # Nested JSON values from 'info'
    print(my_filter.from_csv(path, Keys=["info.skills"]))
    # ['Python', 'Django', 'Excel', 'HR']

    # List stored as string in 'projects'
    print(my_filter.from_csv(path, Keys=["projects"]))
    # ['ERP','Migration','Recruitment','Payroll']

    # Full raw data
    print(my_filter.from_csv(path))
    # [{'id':'1','name':'Amit', ...}, {'id':'2','name':'Neha', ...}]
