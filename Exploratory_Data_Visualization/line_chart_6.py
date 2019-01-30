

# 2 begins here:

import pandas as pd

unrate = pd.read_csv('unrate.csv')

unrate['DATE'] = pd.to_datetime(unrate['DATE'])

#print(unrate.head(12))

#print(unrate.info())





# 6 begins here:

# Let's run this code to see the default properties matplotlib uses.
# If you'd like to follow along on your own computer, we recommend installing
# matplotlib using Anaconda: conda install matplotlib. We recommend working with
# matplotlib using Jupyter Notebook because it can render the plots in the notebook
# itself. You will need to run the following Jupyter magic in a code cell each time
# you open your notebook: %matplotlib inline. Whenever you call show(), the plots will
# be displayed in the output cell. You can read more here.

import matplotlib.pyplot as plt

plt.plot()
plt.show()
















