import pandas as pd

df1 = pd.read_csv('Student_A.csv')
df2 = pd.read_csv('Student_b.csv')
df3 = pd.read_csv('Student_C.csv')
dfAll = pd.concat([df1,df2,df3], axis=1)
print(dfAll)