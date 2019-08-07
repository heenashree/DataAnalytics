
from timeit import default_timer

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')

'''
For first time data load:

Load original CSV files.
Sort by movieId (main key we'll be using) and reset the indices.
Split title and year into separate columns. Convert year to datetime.
Categorize genres properly: split strings into boolean columns per genre.
Modify the rating timestamp: from universal seconds to datetime year.
Check for NaN values. Clean (delete rows) if % of NaN values is small.'''

movies = pd.read_csv('ml-20m/movies.csv')
ratings = pd.read_csv('ml-20m/ratings.csv')

movies.sort_values(by='movieId', inplace=True)
movies.reset_index(inplace=True, drop=True)
ratings.sort_values(by='movieId', inplace=True)
ratings.reset_index(inplace=True, drop=True)
print(movies)
print(ratings)