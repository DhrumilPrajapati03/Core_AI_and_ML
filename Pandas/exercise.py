## 4. Add a New Column

# Given:

# python
# df = pd.DataFrame({
#     "Product": ["Laptop", "Mouse", "Keyboard"],
#     "Price": [50000, 500, 1500]
# })


# Tasks:

# * Create a new column called GST equal to 18% of Price
# * Create a column Final_Price = Price + GST
# * Display the updated DataFrame

import pandas as pd

df = pd.DataFrame({
    "Product": ["Laptop", "Mouse", "Keyboard"],
    "Price": [50000, 500, 1500]
})

# Create a new column called GST equal to 18% of Price
df['GST'] = df['Price'] * (18/100)

# Create a column Final_Price = Price + GST
df['Final_Price'] = df['Price'] + df['GST']

# Display the updated DataFrame
print(df)