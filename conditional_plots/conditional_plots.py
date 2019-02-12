


# 1 begins here:

import pandas as pd

titanic = pd.read_csv('train.csv')
cols = ['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

titanic = titanic[cols].dropna()




# 3 begins here:

import matplotlib.pyplot as plt
import seaborn as sns

# sns.distplot(titanic["Age"])
#
# plt.show()




# 4 begins here:

# sns.kdeplot(titanic["Age"], shade=True)
#
# plt.xlabel("Age")
#
# plt.show()




# 5 begins here:

# sns.set_style('white')
#
# sns.kdeplot(titanic['Age'], shade=True)
#
# sns.despine(left=True, bottom=True)
#
# plt.xlabel('Age')




# 6 begins here:

# g = sns.FacetGrid(titanic, col="Pclass", size=9)
#
# g.map(sns.kdeplot, "Age", shade=True)
#
# sns.despine(left=True, bottom=True)
#
# plt.show()




# 7 begins here:

# g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
# g.map(sns.kdeplot, "Age", shade=True)
# sns.despine(left=True, bottom=True)
# plt.show()




# 8 begins here:

# g = sns.FacetGrid(titanic, col="Survived", row="Pclass")
# g.map(sns.kdeplot, "Age", shade=True)
# sns.despine(left=True, bottom=True)
# plt.show()
# g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex", size=3)
# g.map(sns.kdeplot, "Age", shade=True)
# sns.despine(left=True, bottom=True)
# plt.show()




# 9 begins here:

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue="Sex", size=3)
g.map(sns.kdeplot, "Age", shade=True)
g.add_legend()
sns.despine(left=True, bottom=True)
plt.show()




