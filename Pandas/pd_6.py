# Pivot Tables


import numpy as np
import pandas as pd


data = {
    'Date': pd.date_range('2023-01-01', periods=20),
    'Product': ['A', 'B', 'C', 'D'] * 5,
    'Region': ['East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
    'Sales': np.random.randint(100, 1000, 20),
    'Units': np.random.randint(10, 100, 20),
    'Rep': ['John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice', 'John', 'Mary', 'Bob', 'Alice']
}

df = pd.DataFrame(data)

df['Month'] = df['Date'].dt.month_name()

df['Quarter'] = 'Q' + df['Date'].dt.quarter.astype(str)


#          Date Product Region  Sales  Units    Rep    Month Quarter
# 0  2023-01-01       A   East    266     13   John  January      Q1
# 1  2023-01-02       B   West    445     77   Mary  January      Q1
# 2  2023-01-03       C  North    491     13    Bob  January      Q1
# 3  2023-01-04       D  South    957     66  Alice  January      Q1
# 4  2023-01-05       A   East    932     97   John  January      Q1
# 5  2023-01-06       B   West    752     30   Mary  January      Q1
# 6  2023-01-07       C  North    482     94    Bob  January      Q1
# 7  2023-01-08       D  South    374     48  Alice  January      Q1
# 8  2023-01-09       A   East    616     74   John  January      Q1
# 9  2023-01-10       B   West    729     25   Mary  January      Q1
# 10 2023-01-11       C  North    282     59    Bob  January      Q1
# 11 2023-01-12       D  South    561     41  Alice  January      Q1
# 12 2023-01-13       A   East    863     41   John  January      Q1
# 13 2023-01-14       B   West    678     92   Mary  January      Q1
# 14 2023-01-15       C  North    750     98    Bob  January      Q1
# 15 2023-01-16       D  South    529     19  Alice  January      Q1
# 16 2023-01-17       A   East    919     92   John  January      Q1
# 17 2023-01-18       B   West    637     22   Mary  January      Q1
# 18 2023-01-19       C  North    562     43    Bob  January      Q1
# 19 2023-01-20       D  South    244     91  Alice  January      Q1
# print(df)


# Product      A      B      C      D
# Region
# East     490.2    NaN    NaN    NaN
# North      NaN    NaN  471.4    NaN
# South      NaN    NaN    NaN  557.2
# West       NaN  372.6    NaN    NaN

# by default aggfunc='mean'
nd = pd.pivot_table(data=df, values='Sales', index='Region', columns='Product', aggfunc='median')
# print(nd)


#          Sales                      Units
# Product      A      B      C      D     A     B     C     D
# Region
# East     578.0    NaN    NaN    NaN  37.0   NaN   NaN   NaN
# North      NaN    NaN  840.0    NaN   NaN   NaN  76.0   NaN
# South      NaN    NaN    NaN  355.0   NaN   NaN   NaN  72.0
# West       NaN  830.0    NaN    NaN   NaN  33.0   NaN   NaN
nd1 = pd.pivot_table(data=df, values=['Sales', 'Units'], index='Region', columns='Product', aggfunc='median')
# print(nd1)



# Cross Table -> show only the counts

# Product  A  B  C  D
# Region
# East     5  0  0  0
# North    0  0  5  0
# South    0  0  0  5
# West     0  5  0  0
nd2 = pd.crosstab(df['Region'], df['Product'])
# print(nd2)