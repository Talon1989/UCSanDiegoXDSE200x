import pandas as pd
import numpy as np


# a = [0,1,2,3]
# b = [1,2,3,4]
# for n1, n2 in zip(a,b):
#     print(n1, n2)

# dic = {'tom':1, 'bob':3}
# dic['fabio'] = 123
# try:
#     print(dic['waldo'])
# except KeyError:
#     print('key not found in dictionary')
# dd = {}
# dd['asd'] = [123]
# dd['asd'].append(3)
# print(dd)




# PANDAS SERIES

ser1 = pd.Series(data=[1,2,3], index=['tom', 'bob', 'luc'])
print(ser1)
# data inside series can be heterogeneous
# print( pd.Series([1,2,'boom'], ['tom', 'bob', 'luc']) )  # same
# print()
# ser1.index; ser1.data
print(ser1[['tom','luc']])  # == ser1.loc[['tom','luc']]
print(ser1.iloc[0])  # value with index at 0 position
print(ser1*2)
print()


# PANDAS DATAFRAME

d = {'one': pd.Series([100.,200.,300.]
                      ,['apple','ball','clock'])
     ,'two': pd.Series([111., 222., 333., 4444.]
                       , ['apple', 'ball', 'cerill', 'dancy'])}
df = pd.DataFrame(d)
print(df)  # df.transpose for inverting cols, rows
print(df.index)
print(df.columns)
print(pd.DataFrame(d, index=['apple', 'banana']))
print()
data = [{'balls': 1, 'vases': 2, 'plates': 4}
    , {'balls':5, 'forks':3, 'suitcases':17}]
df = pd.DataFrame(data, index=['p1', 'p2'])
print(df)
df['shoes'] = df['balls'] ** 2
print(df)
print('greater than 2 in column balls: \n', df['balls']>2)
suitcases = df.pop('suitcases')
print('printing suitcases Series:', suitcases)  # suitcases is a series when removed from a dataframe
df2 = df[['balls', 'vases']][:1]  # new df, copy of first value of column balls and vases
print(df2)
print(df.head(1))




