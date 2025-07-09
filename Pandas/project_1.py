import numpy as np
import pandas as pd

# loading the data
# C:\Users\user\Desktop\suresh\Python_Lib\Pandas\posts.csv
df = pd.read_csv(r'posts.csv')
# print(df)


#    Post_id Post_Type  comments  likes
# 0      101  Carousel       268  16382
# 1      102      Reel       138   9267
# 2      103      Reel      1089  10100
# 3      104      Reel       271   6943
# 4      105      Reel       145  17158

df1 = df.head()

# print(df.loc[1]['Post_Type'])


def nameCheck(txt):
    if txt == 'Reel':
        return 'Data In'
    else:
        return 'No Data In'

# print(df1['Post_Type'].apply(nameCheck))

totalComment = df1['comments'].sum()
totalLikes = df1['likes'].sum()

totalCommentLoss = totalLikes - totalComment
# print(totalCommentLoss)

# print(df[df['likes'] == df['likes'].max()])
newData = df[df['likes'] >= 45000]
lst1 = newData['Post_id'].tolist()
print(lst1, len(lst1))