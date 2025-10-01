"""
# ---------------------------- Examples for Search class ----------------------------

# 1️⃣ String list, Lw=True
s1 = Search(MainList=["Andheri", "Versova"])
print(s1.list)        # ['andheri', 'versova']
print(s1.init_error)  # {'status': True, 'details': 'All items processed successfully'}

# 2️⃣ String list, Lw=False
s2 = Search(MainList=["Andheri", "Versova"], Lw=False)
print(s2.list)        # ['Andheri', 'Versova']
print(s2.init_error)  # {'status': True, 'details': 'All items processed successfully'}

# 3️⃣ String tuple
s3 = Search(MainList=("Sakinaka", "Marol Naka"))
print(s3.list)        # ['sakinaka', 'marol naka']
print(s3.init_error)  # {'status': True, 'details': 'All items processed successfully'}

# 4️⃣ String set
s4 = Search(MainList={"Ghatkopar", "Andheri"})
print(s4.list)        # ['ghatkopar', 'andheri']  # set order may vary
print(s4.init_error)  # {'status': True, 'details': 'All items processed successfully'}

# 5️⃣ Dict list with Key
s5 = Search(MainList=[{"name": "Andheri"}, {"name": "Versova"}], Key="name")
print(s5.list)        # ['andheri', 'versova']
print(s5.init_error)  # {'status': True, 'details': 'All items processed successfully'}

# 6️⃣ Dict list missing Key
s6 = Search(MainList=[{"place": "Versova"}], Key="name")
print(s6.list)        # []
print(s6.init_error)  # {'status': False, 'details': "Key 'name' not found in dict {'place': 'Versova'}"}

# 7️⃣ Dict list empty dict
s7 = Search(MainList=[{}], Key="name")
print(s7.list)        # []
print(s7.init_error)  # {'status': False, 'details': 'Dict inside MainList cannot be empty'}

# 8️⃣ Mixed types (string + dict)
s8 = Search(MainList=["Andheri", {"name": "Versova"}])
print(s8.list)        # []
print(s8.init_error)  # {'status': False, 'details': 'All elements must be of same type as first element'}

# 9️⃣ Invalid first element type
s9 = Search(MainList=[123, 456])
print(s9.list)        # []
print(s9.init_error)  # {'status': False, 'details': 'First element must be string or dict'}

# 10️⃣ Empty list
s10 = Search(MainList=[])
print(s10.list)        # []
print(s10.init_error)  # {'status': True, 'details': 'All items processed successfully'}

# 11️⃣ MainList is None
s11 = Search()
print(s11.list)        # []
print(s11.init_error)  # {'status': True, 'details': 'All items processed successfully'}

"""