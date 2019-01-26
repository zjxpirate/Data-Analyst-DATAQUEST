




import pandas as pd

f500 = pd.read_csv("f500.csv")


top_employer_by_country = {}


countries = f500["country"].unique()
print(countries)


for c in countries:
    selected_rows = f500[f500["country"] == c]
    #print(selected_rows)

    sorted_rows = selected_rows.sort_values("employees", ascending=False)
    #print(sorted_rows["country"])

    top_employer = sorted_rows.iloc[0]
    #print(top_employer)

    employer_name = top_employer["company"]
    #print(employer_name)

    top_employer_by_country[c] = employer_name



#print(top_employer_by_country)












