import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
#from wordcloud import WordCloud, STOPWORDS

data = pd.read_csv('ml-20m/movies.csv')
print(data.shape)

#print first 5 movies
print(data.head())
print(data.info())

movies = data['movieId'].unique()
print(len(movies))
print(data.describe())

print(data.isnull().any())

drama_movies = data['genres'].str.contains('Drama')
print(data[drama_movies].head())

#read from ratings data
ratings_data = pd.read_csv('ml-20m/ratings.csv')

movie_data_ratings = data.merge(ratings_data, on='movieId')
print(movie_data_ratings.head())

print(movie_data_ratings['rating']>4.0)
