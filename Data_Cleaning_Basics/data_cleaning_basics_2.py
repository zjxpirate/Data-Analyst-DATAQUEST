

import pandas as pd

#laptops = pd.read_csv("laptops.csv", encoding="UTF-8")
laptops = pd.read_csv("laptops.csv", encoding="Windows-1251")
#laptops = pd.read_csv("laptops.csv", encoding="Latin-1")

#laptops.info()



# 1. Removing any whitespace from the start and end of the labels
# 2. Replacing spaces with underscores and remove special characters - this will make things consistent,
#    and also allows for the use of dot accessors for those who prefer that.
# 3. Make all labels lowercase - this is good for consistency, and means you'll never have to remember
#    what is capitalized and how.
# 4. Shorten any long column names - this helps to keep your code easier to read, especially when you
#    are using method chaining.

#print(laptops.columns)


laptops_test = laptops.copy()
laptops_test.columns = ['A', 'B', 'C', 'D', 'E', 'G', 'F', 'H', 'I', 'J', 'K', 'L', 'M']
#print(laptops_test.columns)





def clean_col(col):
    col = col.strip()
    col = col.replace("(","")
    col = col.replace(")","")
    col = col.lower()
    return col

laptops.columns = [clean_col(c) for c in laptops.columns]






def modify(l1):
    l1 = l1.strip()
    l1 = l1.replace("Operating System", "os")
    l1 = l1.replace(" ", "_")
    l1 = l1.replace("(", "")
    l1 = l1.replace(")", "")
    l1 = l1.lower()
    return l1

laptops.columns = [modify(i) for i in laptops.columns]
print(laptops.columns)

















