# Series

import numpy as np
import pandas as pd 

# index
label = ['a', 'b', 'c']

# creating a series
my_list = [10, 20, 30]

arr = np.array([10, 20, 30])

d = {1:20, 2: 20, 3: 30}

# create series (data and index) need
# print(pd.Series(my_list))

# with using customer series, alphabet
# data = pd.Series(my_list, index=label)
# print(data)

# number series
# data = pd.Series(my_list, index=arr)
# print(data)

# using dict, dict key -> series, and value is -> column data
data = pd.Series(d)
# print(data)