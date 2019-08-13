import pandas as pd

data=pd.read_excel('generation_monthly.xlsx', sheet_name=None)

sheet_names = list(data.keys())
sheet_names = sheet_names[:len(sheet_names)-1]


df_combined=data[sheet_names[0]]
for sheet in sheet_names[1:]:
    df = data[sheet]
    if ('Unnamed: 1' in df.columns):
        df = df.iloc[5:]
        df = df.rename(columns={"U.S. Department of Energy, The Energy Information Administration (EIA)": "YEAR",
        'Unnamed: 1':'MONTH','Unnamed: 2':'STATE','Unnamed: 3':'TYPE OF PRODUCER','Unnamed: 4':'ENERGY SOURCE','Unnamed: 5':'GENERATION (Megawatthours)'})
    df_combined = pd.concat([df_combined,df])

df_combined.to_csv('monthly_electricity_source_data.csv',index=False)