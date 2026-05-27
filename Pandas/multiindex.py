import pandas as pd

df = pd.read_csv("dataclg.csv")
# print(df)
print(type(df))
df.set_index(['Col','Dep','Sem','RN'],inplace=True)
print(df)

# print(df.loc['Darshan','ME'])
print(df.iloc[1])