# Missing Data Frame

import numpy as np
import pandas as pd

# Finding missing data
# Removing missing data
# Filling the missing data


# 1. ------------------------------------------------------------

# np.nan -> return not a number value
data = {    
    'A' : [1, 2, np.nan, 4, 5],
    'B' : [np.nan, 2, 3, 4, 5],
    'C' : [1, 2, 3, np.nan, np.nan],
    'D' : [1, np.nan, np.nan, np.nan, 5]
}

df = pd.DataFrame(data=data)
print(df)

# but not change in actual table because with not user (inplace=True) 


checkBoolValue = df.isna()
# if NaN -> True, everything is False.
# place is empty or not
# print(checkBoolValue)

checkSum = checkBoolValue.sum()
# how many empty place is available 
# A    1
# B    1
# C    2
# D    3
# print(checkSum)

# check null falues present in in any column aur not
# A    True
# B    True
# C    True
# D    True
# null value exist in every column
anyValue = checkBoolValue.any()
# print(anyValue)

# 2. ------------------------------------------------------------------------------

# drop if null value present in row of data
# valueDrop = df.dropna()
# print(valueDrop)

# thresh -> inside a row there should be a non null value = 3
# valueDrop1 = df.dropna(thresh=3)


# 3. ------------------------------------------------------------------------------

valueDf = df.fillna(value=0)
# print(valueDf)

values = {'A' : 0, 'B' : 100, 'C' : 300, 'D' : 400}
valueOf1 = df.fillna(value=values)
# print(valueOf1)

# fill all the column with mean of rows
valueOf3 = df.fillna(df.mean())