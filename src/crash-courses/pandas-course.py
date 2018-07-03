from unittest.mock import inplace

import numpy as np
import pandas as pd
import random





def series():

    labels = ['a', 'b', 'c']
    my_data = [10,20,30]
    d = {}
    for i in range(len(labels)):
        d[labels[i]] = my_data[i]
    print( pd.Series(data=my_data) )  # automatically fills the index as nums 0 +
    print( pd.Series(data=my_data, index=labels) )  # == pd.Series(my_data, labels)
    print( pd.Series(d) )  # passing a dictionary automatically sets data=vals, index=keys
    pd.Series(data=[len,2,'banana',True,12, sum])  # works with different objects / functions

    ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'USSR', 'Japan'])
    ser2 = pd.Series([1,1,1,1], ['USA', 'Germany', 'Italy', 'Japan'])
    print(ser1['USA'])
    print(ser1 + ser2)


def dataFrames1():
    np.random.seed(101)
    df = pd.DataFrame(np.random.randn(5,4),
                      index=['A','B','C','D','E'], columns=['W','X','Y','Z'])
    print(df, type(df))
    df['new'] = df['W']+df['Y']
    print(df)
    df.drop('new', axis=1, inplace=True)  # need to specify 1 as axis since it's a col not row
    print('X=\n', df['W'], type(df['W']))
    print( df[ ['W', 'Z'] ] )  # use basic [] for columns
    print( df.loc[['A','B'],['W','X']] )  # use .loc for index, index + columns
    print( df.iloc[:2, -2:] )  # iloc works just like np.array, use index numbers


def dataFrames2():
    np.random.seed(101)
    df = pd.DataFrame(np.random.randn(5,4),
                      index=['A','B','C','D','E'], columns=['W','X','Y','Z'])
    positive = df > 0  # just like np
    print( positive )
    print( df[positive] )
    print( df['W'] > 0 )
    print( df[df['W'] > 0] )  # returns all the df but not the rows where 'W' > 0
    less0 = df[df['Z'] < 0]  # will only get row C because it's only where Z < 0
    yxOfZLess0 = df[df['Z'] < 0][['Y', 'X']]
    # using multiple conditions
    wAndYCond = df[ (df['W'] > 0) & (df['Y'] > 1) ]  # use & not 'and' since latter cannot handle lists
    print(wAndYCond)
    wOrYCond = df[ (df['W'] > 0) | (df['Y'] > 1) ]  # | for or
    # resetting the index to a numerical value
    wAndYCond.reset_index(inplace=True)
    print(wAndYCond)
    # add a column of data and set the index to that column value
    newind = 'CA NY WY OR CO'.split(' ')
    df['States'] = newind
    print(df)
    df.set_index('States',inplace=True)
    print(df)


def dataFrames3():  # multi index level dataframe
    outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
    inside = [1,2,3,1,2,3]
    # for a,b in zip(outside, inside):
    #     print(a, b)
    hier_index = list(zip(outside, inside))
    hier_index = pd.MultiIndex.from_tuples(hier_index)
    print(hier_index)
    df = pd.DataFrame(np.random.randn(6,2), hier_index, ['A','B'])
    print(df)
    print( df.loc['G1'].loc[2,'B'] )  # -1.4029...
    df.index.names = ['groups', 'num']
    print(df)
    print( df.xs('G1') )   # returns cross section G1
    print( df.xs(1, level='num'))  # returns rows called '1' of column 'num',





dataFrames3()

