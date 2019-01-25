




import pandas as pd

f500 = pd.read_csv("f500.csv")






f500["roa"] = f500["profits"] / f500["assets"]


top_roa_by_sector = {}



for sector in f500["sector"].unique():
    is_sector = f500["sector"] == sector
    print(is_sector)

    sector_companies = f500.loc[is_sector]


    top_company = sector_companies.sort_values("roa", ascending=False).iloc[0]


    company_name = top_company["company"]


    top_roa_by_sector[sector] = company_name




#print(top_roa_by_sector)

