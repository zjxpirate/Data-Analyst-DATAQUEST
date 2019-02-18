

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for f in data_files:
    d = pd.read_csv("schools/{0}".format(f))
    key_name = f.replace(".csv", "")
    data[key_name] = d

# print(data["sat_results"].head())

# for k in data:
#     print(data[k].head())

all_survey = pd.read_csv("schools/survey_all.txt", delimiter="\t",  encoding='windows-1252')

d75_survey = pd.read_csv("schools/survey_d75.txt", delimiter="\t", encoding='windows-1252')

survey = pd.concat([all_survey, d75_survey], axis=0, sort=True)

#print(survey.head())

survey["DBN"] = survey["dbn"]

survey_fields = [
    "DBN",
    "rr_s",
    "rr_t",
    "rr_p",
    "N_s",
    "N_t",
    "N_p",
    "saf_p_11",
    "com_p_11",
    "eng_p_11",
    "aca_p_11",
    "saf_t_11",
    "com_t_11",
    "eng_t_11",
    "aca_t_11",
    "saf_s_11",
    "com_s_11",
    "eng_s_11",
    "aca_s_11",
    "saf_tot_11",
    "com_tot_11",
    "eng_tot_11",
    "aca_tot_11",
]

survey = survey.loc[:,survey_fields]
data["survey"] = survey

#print(survey.head())

data["hs_directory"]["DBN"] = data["hs_directory"]["dbn"]

def pad_csd(num):
    string_representation = str(num)
    if len(string_representation) > 1:
        return string_representation
    else:
        return string_representation.zfill(2)

data["class_size"]["padded_csd"] = data["class_size"]["CSD"].apply(pad_csd)
data["class_size"]["DBN"] = data["class_size"]["padded_csd"] + data["class_size"]["SCHOOL CODE"]
#print(data["class_size"].head())

cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']

for c in cols:
    data["sat_results"][c] = pd.to_numeric(data["sat_results"][c], errors="coerce")

data['sat_results']['sat_score'] = data['sat_results'][cols[0]] + data['sat_results'][cols[1]] + data['sat_results'][cols[2]]

#print(data['sat_results']['sat_score'].head())

import re

def find_lat(loc):
    coords = re.findall("\(.+\)", loc)
    lat = coords[0].split(",")[0].replace("(", "")
    return lat

data["hs_directory"]["lat"] = data["hs_directory"]["Location 1"].apply(find_lat)

#print(data["hs_directory"].head())

def find_lon(loc):
    coords = re.findall("\(.+\)", loc)
    lon = coords[0].split(",")[1].replace(")", "").strip()
    return lon

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(find_lon)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")

#print(data["hs_directory"].head())




# 3 begins here:

class_size = data["class_size"]

class_size = class_size[class_size["GRADE "] == "09-12"]

class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]

#print(class_size.head())

# 5 begins here:

import numpy

class_size = class_size.groupby("DBN").agg(numpy.mean)

class_size.reset_index(inplace=True)

data["class_size"] = class_size

#print(data["class_size"].head())

# 7 begins here:

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]

#print(data["demographics"].head())

# 9 begins here:

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]
#print(data["graduation"].head())

# 10 begins here:

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']

for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col], errors="coerce")

#print(data["ap_2010"].dtypes)

# 12 begins here:

combined = data["sat_results"]

combined = combined.merge(data["ap_2010"], on = "DBN", how = "left")

combined = combined.merge(data["graduation"], on="DBN", how="left")

# print(combined.head(5))
# print(combined.shape)

# 13 begins here:

to_merge = ["class_size", "demographics", "survey", "hs_directory"]

for m in to_merge:
    combined = combined.merge(data[m], on="DBN", how="inner")

# print(combined.head(5))
# print(combined.shape)

# 15 begins here:

combined = combined.fillna(combined.mean())

combined = combined.fillna(0)

#print(combined.head(5))

# 16 begins here:

def get_first_two_chars(dbn):
    return dbn[0:2]

combined["school_dist"] = combined["DBN"].apply(get_first_two_chars)

#print(combined["school_dist"].head())

























# Data_Cleaning_Walkthrough_Analyzing_and_Visualizing_the_Data


# 3 begins here:

correlations = combined.corr()

correlations = correlations["sat_score"]

#print(correlations)




# 5 begins here:

import matplotlib.pyplot as plt

#combined.plot.scatter(x='total_enrollment', y='sat_score')

#plt.show()





# 6 begins here:

low_enrollment = combined[combined["total_enrollment"] < 1000]

low_enrollment = low_enrollment[low_enrollment["sat_score"] < 1000]

#print(low_enrollment["School Name"])





# 7 begins here:

#combined.plot.scatter(x='ell_percent', y='sat_score')

#plt.show()





# 9 begibs here:

# from mpl_toolkits.basemap import Basemap
#
# m = Basemap(
#     projection='merc',
#     llcrnrlat=40.496044,
#     urcrnrlat=40.915256,
#     llcrnrlon=-74.255735,
#     urcrnrlon=-73.700272,
#     resolution='i'
# )
#
# m.drawmapboundary(fill_color='#85A6D9')
# m.drawcoastlines(color='#6D5F47', linewidth=.4)
# m.drawrivers(color='#6D5F47', linewidth=.4)
#
# longitudes = combined["lon"].tolist()
# latitudes = combined["lat"].tolist()
# m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True)
# plt.show()





# 10 begins here:

# from mpl_toolkits.basemap import Basemap
#
# m = Basemap(
#     projection='merc',
#     llcrnrlat=40.496044,
#     urcrnrlat=40.915256,
#     llcrnrlon=-74.255735,
#     urcrnrlon=-73.700272,
#     resolution='l'
# )
#
# m.drawmapboundary(fill_color='#85A6D9')
# m.drawcoastlines(color='#6D5F47', linewidth=.4)
# m.drawrivers(color='#6D5F47', linewidth=.4)
#
# longitudes = combined["lon"].tolist()
# latitudes = combined["lat"].tolist()
#
# m.scatter(longitudes, latitudes, s=20, zorder=2, latlon=True, c=combined["ell_percent"], cmap="summer")

#plt.show()




# 11 begins here:

import numpy

districts = combined.groupby("school_dist").agg(numpy.mean)
districts.reset_index(inplace=True)
print(districts.head())




# 12 begins here:

from mpl_toolkits.basemap import Basemap

m = Basemap(
    projection='merc',
    llcrnrlat=40.496044,
    urcrnrlat=40.915256,
    llcrnrlon=-74.255735,
    urcrnrlon=-73.700272,
    resolution='l'
)

m.drawmapboundary(fill_color='#85A6D9')
m.drawcoastlines(color='#6D5F47', linewidth=.4)
m.drawrivers(color='#6D5F47', linewidth=.4)

longitudes = districts["lon"].tolist()
latitudes = districts["lat"].tolist()
m.scatter(longitudes, latitudes, s=50, zorder=2, latlon=True, c=districts["ell_percent"], cmap="summer")
plt.show()



