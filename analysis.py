import pandas as pd
df=pd.read_csv("electeicity_demand.csv",encoding="latin1")
print(df.head())
print(df.columns.tolist())
print (df.info())
