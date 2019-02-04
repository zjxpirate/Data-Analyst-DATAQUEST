

# 2 begins here:
import pandas as pd

reviews = pd.read_csv("fandango_scores.csv")

cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]
#print(norm_reviews[:1])





# 4 begins here:

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75

# fig, ax = plt.subplots()
#
# ax.bar(bar_positions, bar_heights, 0.5)
#
# plt.show()







# 5 begins here:

num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
bar_heights = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)

# fig, ax = plt.subplots()
#
# ax.bar(bar_positions, bar_heights, 0.5)
# ax.set_xticks(tick_positions)
# ax.set_xticklabels(num_cols, rotation=90)
#
# ax.set_xlabel('Rating Source')
# ax.set_ylabel('Average Rating')
# ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
# plt.show()






# 6 begins here:

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

bar_widths = norm_reviews[num_cols].iloc[0].values
bar_positions = arange(5) + 0.75
tick_positions = range(1,6)



# fig, ax = plt.subplots()
# ax.barh(bar_positions, bar_widths, 0.5)
#
# ax.set_yticks(tick_positions)
# ax.set_yticklabels(num_cols)
# ax.set_ylabel('Rating Source')
# ax.set_xlabel('Average Rating')
# ax.set_title('Average User Rating For Avengers: Age of Ultron (2015)')
# plt.show()






# 7 begins here:

# fig, ax = plt.subplots()
#
# ax.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
#
# ax.set_xlabel('Fandango')
#
# ax.set_ylabel('Rotten Tomatoes')
#
# plt.show()






# 8 brgins here:

fig = plt.figure(figsize=(5,10))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
reviews = pd.read_csv('fandango_scores.csv')
cols = ['FILM', 'RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']
norm_reviews = reviews[cols]


ax1.scatter(norm_reviews['Fandango_Ratingvalue'], norm_reviews['RT_user_norm'])
ax1.set_xlabel('Fandango')
ax1.set_ylabel('Rotten Tomatoes')
ax2.scatter(norm_reviews['RT_user_norm'], norm_reviews['Fandango_Ratingvalue'])
ax2.set_xlabel('Rotten Tomatoes')
ax2.set_ylabel('Fandango')
plt.show()













