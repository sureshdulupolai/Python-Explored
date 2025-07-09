import numpy as np
import pandas as pd 

# Creating a DataFrames
# Selection and indexing of columns
# Creating a new column
# Removing Columns
# Selecting Rows
# Selecting Subsets of rows and columns
# Conditional selection


# 1. -----------------------------------------------------------------------------
data = {
    'Name' : ['John', 'Anna', 'Peter', 'Linda'],
    'Age' : [28, 34, 29, 42],
    'City' : ['New York', 'Paris', 'Berlin', 'London'],
    'Salary' : [65000, 70000, 62000, 85000]
}

# dataIn = pd.DataFrame(data=data)
# print(dataIn)

data_list = [
    ['John', 28, 'New York', 65000],
    ['Anna', 34, 'Paris', 70000],
    ['Peter', 29, 'Berlin', 62000],
    ['Linda', 42, 'London', 85000]
]

# by default, header aur column name comes in default (0, 1, 2, 3)
# df2 = pd.DataFrame(data=data_list)
# print(df2)

columns = ['Name', 'Age', 'City', 'Salary']
df3 = pd.DataFrame(data=data_list, columns=columns)
# print(df3)

# 2. -----------------------------------------------------------------------------------

# for target column, single column
# print(df3['Name'])


# multiple column target
# print(df3[['Name', 'City']])


# 3. ------------------------------------------------------------------------------------

df3["Designation"] = ['Doctor', 'Eng.', 'Doctor', 'Eng.']
# print(df3)


# dont run all because it can show error to column not found

# drop a column, axis = 0 -> find "Designation" in up to down, axis = 1 is left to right in header
# df3.drop("Designation", axis=1)
# print(df3) # showing copy

# df3.drop("Designation", axis=1, inplace=True)
# print(df3) # orginal column remove

# multiple 
# df3.drop(["City", "Designation"], axis=1, inplace=True)


# 4. -------------------------------------------------------------------------------------
# data = df3.loc[[0, 1]][["City", "Salary"]]
# print(data)


# last -----------------------------------------------------------------------------------


# i only want to see the people whose age is above 30 and city is paris
dataIn = df3[(df3["Age"] > 30) & (df3['City'] == 'Paris')]
print(dataIn)