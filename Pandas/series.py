#syntax
# import pandas as pd
# s = pd.Series(data,index,dtype,copy=False)

import pandas as pd
s = pd.Series([1, 3, 5, 7, 9, 11])
print(s)

print("S[0] = ", s[0])
b = s[0] + s[1]
print("Sum = ", b)

k = pd.Series([1, 3, 5, 7, 9, 11], dtype=str)
print("S[0] = ", s[0])
b = k[0] + k[1]
print("Sum = ", b)