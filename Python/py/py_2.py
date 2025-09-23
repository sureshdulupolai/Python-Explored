students = [
    {"name": "Amit", "age": 21, "marks": 85},
    {"name": "Riya", "age": 20, "marks": 92},
    {"name": "Sohan", "age": 22, "marks": 70},
    {"name": "Anita", "age": 19, "marks": 60},
    {"name": "Karan", "age": 21, "marks": 76},
]

# Questions (choose any 👇 and solve with lambda)

# Sort students by marks (high to low).
# Filter out students who scored more than 75.
# Get only names of students using map. [ map(function, iterable) ]
# Find student with minimum marks.
# Calculate sum of all marks.


students.sort(key=lambda st: -st['marks'])
print(students)

# 75 se zyada marks wale students filter karna
top_students = list(filter(lambda a: a["marks"] > 75, students))
print(list(reversed(top_students)))

print(list(map(lambda a: a['name'], students)))

print(sum(list(map(lambda a: a['marks'], students))))