import numpy as np
import pandas as pd

np.random.seed(1)
arr = np.random.randint(1,100,20).reshape(5,4)
df = pd.DataFrame(arr,np.arange(101,106,1),['maths','science', 'bio', 'programming'])
print(df)
print(type(df))
print(df[df>50])
print(df.ndim)

# print(df['bio'])
# print(df[['bio','science']])

# print(df.loc[101])

# print(df.iloc[2])

# df.drop(101,inplace=True)
# print(df)

# df.drop('bio', axis=1, inplace=True)
# print(df)

print(df.loc[[101,102], ['maths','science']])

# df['total'] = df['maths'] + df['science'] + df['bio'] + df['programming']
# print(df)

