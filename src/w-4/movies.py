import pandas as pd
pd.set_option('display.max_columns', None)

movielens_absolute_path = 'C:/Users/Talon/Desktop/py/jupyter notebooks/movielens'

movies = pd.read_csv(movielens_absolute_path+'/movies.csv', sep=',')
print(type(movies))  # DataFrame

tags = pd.read_csv(movielens_absolute_path+'/tags.csv', sep=',')
del tags['timestamp']

movie_row_0 = movies.iloc[0]
print(movie_row_0)
# some_movies = movies.iloc[ [0,15,123] ]
first_10_movies = movies.iloc[ 0:10 ]

