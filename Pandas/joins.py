import pandas as pd

# 1. Recreate the base allStudent dataframe from previous example
dfCX = pd.read_csv('Student_A.csv', index_col=0)
dfCY = pd.read_csv('Student_b.csv', index_col=0)
dfCZ = pd.read_csv('Student_C.csv', index_col=0)
allStudent = pd.concat([dfCX, dfCY, dfCZ])
print(allStudent)

# 2. Read the new join target
dfINS = pd.read_csv('IS.csv', index_col=0)

# # 3. Perform and print operations
dfLeftJoin = allStudent.join(dfINS)
# print("--- Output-1 (Left Join) ---")
print(dfLeftJoin)

dfRightJoin = allStudent.join(dfINS, how='right')
# print("\n--- Output-2 (Right Join) ---")
print(dfRightJoin)

