

# 1 begins here:

import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')

# unrate['DATE'] = pd.to_datetime(unrate['DATE'])
#
# first_twelve = unrate[0:12]
#
# plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
#
# plt.xticks(rotation=0)
#
# plt.xlabel('Month')
#
# plt.ylabel('Unemployment Rate')
#
# plt.title('Monthly Unemployment Trends, 1948')

#plt.show()






# 2 begins here:

#fig = plt.figure()

#ax1 = fig.add_subplot(2,1,1)
#ax2 = fig.add_subplot(2,1,2)

#plt.show()





# 3 begins here:

# fig = plt.figure()
#
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)

#plt.show()





# 5 begins here:
#
# fig = plt.figure()
# ax1 = fig.add_subplot(2,1,1)
# ax2 = fig.add_subplot(2,1,2)
#
# ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
# ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
#
# plt.show()






# 6 begins here:

fig = plt.figure(figsize=(15, 8))
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()














































