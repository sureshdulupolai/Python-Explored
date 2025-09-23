companies = [
    {
        "name": "TechSoft",
        "location": "Bangalore",
        "employees": [
            {"name": "Amit", "age": 25, "role": "Developer", "salary": 60000},
            {"name": "Riya", "age": 28, "role": "Manager", "salary": 90000},
            {"name": "Sohan", "age": 24, "role": "Developer", "salary": 55000},
        ]
    },
    {
        "name": "DataCorp",
        "location": "Hyderabad",
        "employees": [
            {"name": "Anita", "age": 26, "role": "Data Scientist", "salary": 75000},
            {"name": "Karan", "age": 30, "role": "Manager", "salary": 95000},
            {"name": "Neha", "age": 27, "role": "Developer", "salary": 58000},
        ]
    },
    {
        "name": "FinSolve",
        "location": "Mumbai",
        "employees": [
            {"name": "Vikas", "age": 29, "role": "Analyst", "salary": 62000},
            {"name": "Priya", "age": 31, "role": "Manager", "salary": 100000},
            {"name": "Arjun", "age": 23, "role": "Intern", "salary": 20000},
        ]
    }
]


# 📌 Questions for Practice (lambda ke saath karo)

# 🔹 Easy
# Har company ke sirf employee names list banao.
# Sabhi employees me se salary > 60,000 wale filter karo.
# Employees ke sirf role list nikalna (duplicate ho sakte hain).

# 🔹 Medium
# Sabhi employees ka total salary nikalna.
# Employees ko salary ke hisaab se sort karna (descending).
# Sirf Developers ke naam aur salary nikalna.

# 🔹 Advanced
# Har company ka highest paid employee ka naam nikalna.
# Sabhi companies ke employees me se youngest employee ka naam.
# Har company me Manager ki salary ka list nikalna.
# Sabhi employees me se ek dict banao jisme role: count ho (kitne Developers, Managers, etc.).


# lstOfCompany = list(map(lambda a: a['name'], companies))
# print(lstOfCompany)

# lstOfEmployees = list(map(lambda b: b['employees'], companies))
# print(lstOfEmployees)


# lst = []
# for i in companies:
#     name = i['name']
#     lstOfEmp = []
#     for j in i['employees']:
#         lstOfEmp += [j['name']]
#     lst += [((name), lstOfEmp)]
# # print(lst)


# lst = list(
#     map(
#         lambda c: (c['name'], list(map(lambda e: e['name'], c['employees']))),
#         companies
#     )
# )

# # print(lst)

# lst = []
# for c in companies:
#     lst.append((c['name'], [e['name'] for e in c['employees']]))


salary_1 = []
for i in companies:
    salary_1.append((i['name'], [j for j in i['employees'] if j['salary'] > 60000]))
# print(salary_1)

for j in salary_1:
    print(j)
    