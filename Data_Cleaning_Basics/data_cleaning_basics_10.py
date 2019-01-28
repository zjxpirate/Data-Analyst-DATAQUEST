



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
#print(laptops.columns)

#print("Type: ", laptops["screen_size"].dtype)
#print(laptops["screen_size"].unique())

laptops["screen_size"] = laptops["screen_size"].str.replace('"','')
#print(laptops["screen_size"].unique())

laptops["screen_size"] = laptops["screen_size"].astype(float)
#print(laptops["screen_size"].dtype)
#print(laptops["screen_size"].unique())

laptops.rename({"screen_size": "screen_size_inches"}, axis=1, inplace=True)
#print(laptops.dtypes)

#print(laptops["ram"].unique())

laptops["ram"] = laptops["ram"].str.replace('GB', '')

laptops["ram"] = laptops["ram"].astype(int)

laptops.rename({"ram": "ram_gb"}, axis=1, inplace=True)

dtypes = laptops.dtypes


#laptops["weight"] = (laptops["weight"].str.replace("kg","").astype(float))
#print(laptops.loc[laptops["weight"].str.contains('s'), "weight"])

#print(laptops["price_euros"].unique()[:5])
#print(laptops["price_euros"].unique()[-5:])

laptops["weight"] = laptops["weight"].str.replace("kgs", "").str.replace("kg", "")
laptops["weight"] = laptops["weight"].astype(float)
laptops.rename({"weight": "weight_kg"}, axis=1, inplace=True)

laptops["price_euros"] = laptops["price_euros"].str.replace(",", ".")
laptops["price_euros"] = laptops["price_euros"].astype(float)

weight_describe = laptops["weight_kg"].describe()
price_describe = laptops["price_euros"].describe()





# 5 begins here:

result = laptops["gpu"].head()

result = laptops["gpu"].head().str.split()

result = laptops["gpu"].head().str.split(n=1)

result = laptops["gpu"].head().str.split(n=1, expand=True)

result = laptops["gpu"].head().str.split(n=1, expand=True).iloc[:, 0]

result = laptops["cpu"].head(10)

laptops["cpu_manufacturer"] = (laptops["cpu"].str.split(n=1, expand=True).iloc[:,0])

#print(laptops)





# 6 begins here:

result = laptops["screen"].unique().shape
result = laptops["screen"].unique()[:10]
result = laptops.loc[:9, "screen"].str.split(expand=True)

result = laptops.loc[:9, "screen"].str.rsplit(n=1, expand=True)

result = laptops["screen"].str.rsplit(n=1, expand=True)
result.columns = ["A", "B"]
result.loc[result["B"].isnull(), "B"] = result["A"]

laptops["screen_resolution"] = result["B"]
#print(laptops["screen_resolution"].unique())

result = laptops["cpu"].unique()[:5]

laptops["cpu_speed_ghz"] = laptops["cpu"].str.replace("GHz", "").str.rsplit(n=1, expand=True).iloc[:,1].astype(float)

#print(laptops.loc[:10, "cpu_speed_ghz"])






# 7 begins here:

#print(laptops["operating_system"].value_counts())

mapping_dict = {
    'Android': 'Android',
    'Chrome OS': 'Chrome OS',
    'Linux': 'Linux',
    'Mac OS': 'macOS',
    'No OS': 'No OS',
    'Windows': 'Windows',
    'macOS': 'macOS'
}

laptops["operating_system"] = laptops["operating_system"].map(mapping_dict)

#print(laptops["operating_system"].unique())




# 8 begins here:

#print(laptops.info())

#print(laptops.isnull().sum())
laptops_no_null_rows = laptops.dropna()
laptops_no_null_cols = laptops.dropna(axis=1)

#print(laptops_no_null_rows)

#print(laptops_no_null_cols)





# 9 begins here:

#print(laptops["operating_system_version"].value_counts(dropna=False))

os_with_null_v = laptops.loc[laptops["operating_system_version"].isnull(), "operating_system"]

#print(os_with_null_v.value_counts())

mac_os_versions = laptops.loc[laptops["operating_system"] == "macOS", "operating_system_version"]

laptops.loc[laptops["operating_system"] == "macOS", "operating_system_version"] = "X"

#print(mac_os_versions.value_counts(dropna=False))

#print(laptops.loc[laptops["operating_system"] == "macOS", "operating_system_version"])





# 10 begins here:

print(laptops.loc[76:81, "storage"])


# replace 'TB' with 000 and rm 'GB'
laptops["storage"] = laptops["storage"].str.replace('GB','').str.replace('TB','000')

# split out into two columns for storage
laptops[["storage_1", "storage_2"]] = laptops["storage"].str.split("+", expand=True)

for s in ["storage_1", "storage_2"]:
    s_capacity = s + "_capacity_gb"
    s_type = s + "_type"
    # create new cols for capacity and type
    laptops[[s_capacity, s_type]] = laptops[s].str.split(n=1,expand=True)
    # make capacity numeric (can't be int because of missing values)
    laptops[s_capacity] = laptops[s_capacity].astype(float)
    # strip extra white space
    laptops[s_type] = laptops[s_type].str.strip()

# remove unneeded columns
laptops.drop(["storage", "storage_1", "storage_2"], axis=1, inplace=True)

print(laptops.loc[76:81, ["storage_1_capacity_gb", "storage_1_type"]])

print(laptops.loc[76:81, ["storage_2_capacity_gb", "dtorage_2_type"]])










