

# 1 begins here:

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

unrate['DATE'] = pd.to_datetime(unrate['DATE'])

first_twelve = unrate[0:12]

plt.plot(first_twelve['DATE'], first_twelve['VALUE'])

plt.xticks(rotation=0)

plt.xlabel('Month')

plt.ylabel('Unemployment Rate')

plt.title('Monthly Unemployment Trends, 1948')

#plt.show()






# 2 begins here:

fig = plt.figure()

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

plt.show()











































