# Group By Aggregation

import numpy as np
import pandas as pd 

data = {
    'Category' : ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Store' : ['S1', 'S1', 'S2', 'S2', 'S1', 'S2', 'S2', 'S1'],
    'Sales' : [100, 200, 150, 250, 120, 180, 200, 300],
    'Quantity' : [10, 15, 12, 18, 8, 20, 15, 25],
    'Date' : pd.date_range('2023-01-01', periods=8)
}

df = pd.DataFrame(data=data)
# print(df)

# Group by Category and calculate the sum of sales
newData = df.groupby('Category')
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000002B81EF586E0> return object
# print(newData) 

# for i, v in newData:
#     print(i) # print A, B Column Name
#     print(v) # full data with header

newData = df.groupby('Category')['Sales'].sum()
# print(newData)


# Group by store and calculate the sum of sales
newData = df.groupby('Store')['Sales'].sum()
# print(newData)


# Group by multiple columns
# Group by category and store
# Category  Store
# A         S1       220
#           S2       350
# B         S1       500
#           S2       430
newData = df.groupby(['Category', 'Store'])['Sales'].sum()
# print(newData)



# Aggregation
# total of mean is now as agg.

ndata = df['Sales'].mean()
# print(ndata) # 187.5

# mode not work
""" 
mean, median, min, max, count, std
"""

nData = df['Sales'].agg(['mean', 'min', 'max'])
print(nData)