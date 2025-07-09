# Merging Joining Concatination


import numpy as np
import pandas as pd 


# Merging 2 dataframes
# Concatination of 2 dataframes
# Joining of 2 dataframes

employees = pd.DataFrame({
    'employee_id' : [1, 2, 3, 4, 5],
    'name' : ['John', 'Anna', 'Peter', 'Linda', 'Bob'],
    'department' : ['HR', 'IT', 'Finance', 'IT', 'HR']
})

salaries = pd.DataFrame({
    'employee_id' : [1, 2, 3, 6, 7],
    'salary' : [60000, 80000, 65000, 70000, 90000],
    'bonus' : [5000, 10000, 7000, 8000, 12000]
})

df = pd.merge(employees, salaries)

df = pd.merge(employees, salaries, on='employee_id')

# by default on take = 'employee_id', by default how='inner'
# 1, 2, 3
df = pd.merge(employees, salaries, on='employee_id', how='inner')
# show only matching query of id
# print(df)

# show all matching query and not matching query with both table if data is not present then show NaN
# 1, 2, 3, 4, 5, 6, 7
df = pd.merge(employees, salaries, on='employee_id', how='outer')
# print(df)

# show matching query from both table and also null value assign for employees table 
# 1, 2, 3, 4, 5
df = pd.merge(employees, salaries, on='employee_id', how='left')
# print(df)

# show data from salaries table
# 1, 2, 3, 6, 7
df = pd.merge(employees, salaries, on='employee_id', how='left')
# print(df)


# 2. -------------------------------------------------------------------------

df1 = pd.DataFrame({
    'A' : ['A0', 'A1', 'A2'],
    'B' : ['B0', 'B1', 'B2'],
    'C' : ['C0', 'C1', 'C2']
})

df2 = pd.DataFrame({
    'A' : ['A3', 'A4', 'A5'],
    'B' : ['B3', 'B4', 'B5'],
    'C' : ['C3', 'C4', 'C5']
})

# column base
#     A   B   C
# 0  A0  B0  C0
# 1  A1  B1  C1
# 2  A2  B2  C2
# 0  A3  B3  C3
# 1  A4  B4  C4
# 2  A5  B5  C5
df = pd.concat([df1, df2])
# print(df)

# row base, axis by default = 0
#     A   B   C   A   B   C
# 0  A0  B0  C0  A3  B3  C3
# 1  A1  B1  C1  A4  B4  C4
# 2  A2  B2  C2  A5  B5  C5
df = pd.concat([df1, df2], axis=1)
# print(df)



# 3. -----------------------------------------------------------------------

df1 = pd.DataFrame({
    'name' : ['Alice', 'Bob', 'Charlie']
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    'score' : [85, 90, 75]
}, index=[2, 3, 4])

# how='inner' by default
#       name  score
# 1    Alice    NaN
# 2      Bob   85.0
# 3  Charlie   90.0
df = df1.join(df2)
# print(df)

