# Operations


import numpy as np
import pandas as pd

df1 = pd.DataFrame({
    'A' : [1, 2, 3, 4, 5],
    'B' : [10, 20, 30, 40, 50],
    'C' : [100, 200, 300, 400, 500]
})

# print(df1)

# Data pre-process

# to find a shape o table, shape is not a function
# print(df1.shape) # (5, 3)




# find column
# Index(['A', 'B', 'C'], dtype='object')
# print(df1.columns)



# find info
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 3 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   A       5 non-null      int64
#  1   B       5 non-null      int64
#  2   C       5 non-null      int64
# dtypes: int64(3)
# memory usage: 252.0 bytes
# None

# print(df1.info())


# find describe
#               A          B           C
# count  5.000000   5.000000    5.000000
# mean   3.000000  30.000000  300.000000
# std    1.581139  15.811388  158.113883
# min    1.000000  10.000000  100.000000
# 25%    2.000000  20.000000  200.000000
# 50%    3.000000  30.000000  300.000000
# 75%    4.000000  40.000000  400.000000
# max    5.000000  50.000000  500.000000

# print(df1.describe())


# adding some value in column 'A'
# print(df1['A'] + 10)


def squareN(x):
    return x**2

df1['B'] = df1['B'].apply(squareN)
df1['D'] = df1['A'].apply(squareN)
df1['E'] = df1['C'].apply(lambda x : x + 10)
# print(df1)
