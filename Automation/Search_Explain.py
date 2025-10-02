"""
# ----------------------------
# 1️⃣ String list, lowercase (default Lw=True)
s1 = Search(MainList=["Andheri", "Versova"])
print(s1.list)
# Output: ['andheri', 'versova']
print(s1.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# ----------------------------
# 2️⃣ String list, no lowercase (Lw=False)
s2 = Search(MainList=["Andheri", "Versova"], Lw=False)
print(s2.list)
# Output: ['Andheri', 'Versova']
print(s2.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# ----------------------------
# 3️⃣ String tuple
s3 = Search(MainList=("Sakinaka", "Marol Naka"))
print(s3.list)
# Output: ['sakinaka', 'marol naka']
print(s3.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# ----------------------------
# 4️⃣ String set
s4 = Search(MainList={"Ghatkopar", "Andheri"})
print(s4.list)
# Output: ['ghatkopar', 'andheri']  # order may vary due to set
print(s4.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# ----------------------------
# 5️⃣ Dict list with Key
s5 = Search(MainList=[{"name": "Andheri"}, {"name": "Versova"}], Key="name")
print(s5.list)
# Output: ['andheri', 'versova']
print(s5.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# ----------------------------
# 6️⃣ Dict list missing Key
s6 = Search(MainList=[{"place": "Versova"}], Key="name")
print(s6.list)
# Output: []
print(s6.init_error)
# Output: {'status': False, 'details': "Key 'name' not found in dict {'place': 'Versova'}", 'Project-Name': 'my_project'}

# ----------------------------
# 7️⃣ Dict list with empty dict
s7 = Search(MainList=[{}], Key="name")
print(s7.list)
# Output: []
print(s7.init_error)
# Output: {'status': False, 'details': 'Dict inside MainList cannot be empty', 'Project-Name': 'my_project'}

# ----------------------------
# 8️⃣ Mixed types (string + dict)
s8 = Search(MainList=["Andheri", {"name": "Versova"}])
print(s8.list)
# Output: []
print(s8.init_error)
# Output: {'status': False, 'details': 'All elements must be of same type as first element', 'Project-Name': 'my_project'}

# ----------------------------
# 9️⃣ Invalid first element type (non-string/dict)
s9 = Search(MainList=[123, 456])
print(s9.list)
# Output: []
print(s9.init_error)
# Output: {'status': False, 'details': 'Elements must be string or dict', 'Project-Name': 'my_project'}

# ----------------------------
# 10️⃣ Empty list
s10 = Search(MainList=[])
print(s10.list)
# Output: []
print(s10.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# ----------------------------
# 11️⃣ MainList is None
s11 = Search()
print(s11.list)
# Output: []
print(s11.init_error)
# Output: {'status': True, 'details': 'All items processed successfully', 'Project-Name': 'my_project'}

# ----------------------------
# 12️⃣ Appending new data to existing project
s12 = Search(MainList=["Marol"], ProjectName="my_project")
print(s12.list)
# Output: ['andheri', 'versova', 'marol']  # previously created list is appended

# ----------------------------
# 13️⃣ Single search (substring or prefix)
result = s1._Search__single__("And")
print(result)
# Output: {'search': ['andheri'], 'find': 1, 'count': 1}

# ----------------------------
# 15️⃣ Show all projects
print(Search.show_all_projects())
# Output: [{'Project-Name': 'my_project', 'details': ['andheri', 'versova', 'marol']}]


# -------------------- 🔹 Sample Data --------------------
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

# -------------------- 🔹 Single Key Examples --------------------

# Nested tuple → convert to string
print(__dict_choice__(data, Keys="students.scores"))
# ['95','88','76','78','85','82']

# Single string value
print(__dict_choice__(data, Keys="class"))
# ['Python Basics']

# List of strings
print(__dict_choice__(data, Keys="topics"))
# ['dict','list','tuple']

# Integer/boolean → convert to string
print(__dict_choice__(data, Keys="meta.year"))
# ['2025']
print(__dict_choice__(data, Keys="meta.active"))
# ['True']

# Set → convert to string
print(__dict_choice__(data, Keys="misc.sets"))
# ['1','2','3']  # order may vary

# -------------------- 🔹 Multiple Keys Examples --------------------

# Extract both class name and student scores at once
print(__dict_choice__(data, Keys=["class", "students.scores"]))
# ['Python Basics', '95','88','76','78','85','82']

# Extract topics and meta year
print(__dict_choice__(data, Keys=["topics", "meta.year"]))
# ['dict','list','tuple','2025']

# Using repeat=True to remove duplicates if same data appears in multiple dicts
data2 = [data, data]  # list of two identical dicts
print(__dict_choice__(data2, Keys=["class","students.scores"], repeat=True))
# ['Python Basics','95','88','76','78','85','82']

# -------------------- 🔹 Strict Type Check --------------------

# Fail if non-string encountered
print(__dict_choice__(data, Keys=["students.scores"], type=False))
# {'error': 'Non-string value found: 95', 'status': 'fail'}

# -------------------- 🔹 Error Cases --------------------

# Key path does not exist
print(__dict_choice__(data, Keys=["students.age"]))
# {'error': "Key path 'students.age' not found in dict {...}", 'status': 'fail'}




# ---------------- Example Usage Of History Class ----------------
history_data = ["Login", "Search: Python", "Open File", "Run Script", "Logout"]

# Create History object
hist = History(history_data)

# 1️⃣ Full history (most recent first)
print("Full History (__all_):", hist.__all_())
# Output: ['Logout', 'Run Script', 'Open File', 'Search: Python', 'Login']

print("Full History (all):", hist.all())
# Output: ['Logout', 'Run Script', 'Open File', 'Search: Python', 'Login']

# 2️⃣ Navigation
print("Next item:", hist.next())
# Output: 'Logout'
print("Next item:", hist.next())
# Output: 'Run Script'
print("Previous item:", hist.previous())
# Output: 'Logout'

# 3️⃣ Access first, last, middle
print("First item (__first_):", hist.__first_())
# Output: 'Login'
print("Last item (__last_):", hist.__last_())
# Output: 'Logout'
print("Middle item (__middle_):", hist.__middle_())
# Output: 'Open File'

# 4️⃣ Aliases all work
print("Middle item (middle):", hist.middle())
# Output: 'Open File'
print("Last item (last):", hist.last())
# Output: 'Logout'
print("First item (first):", hist.first())
# Output: 'Login'

# 5️⃣ Index navigation continues from previous position
print("Next item after last previous call:", hist.next())
# Output: 'Run Script' (index continues)
print("Next item:", hist.next())
# Output: 'Open File'
print("Next item:", hist.next())
# Output: 'Search: Python'
print("Next item:", hist.next())
# Output: 'Login'
print("Next item (beyond end):", hist.next())
# Output: None

"""