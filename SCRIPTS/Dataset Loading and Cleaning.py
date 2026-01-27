# Step 1: Loading the dataset and understanding the column selection

import pandas as pd
# Load the dataset to get column names

df = pd.read_csv('SupplyChainDataset.csv', encoding='ISO-8859-1')
print(df.columns.tolist())
print(df.info())

import pandas as pd

# Load the dataset
# Based on the previous output, it seems the entire row might be quoted or there's a delimiter issue.
# Let's try reading it normally first and check the columns again.

df = pd.read_csv('Supplychain project.csv', encoding='ISO-8859-1')

# Check if the dataframe has only one column (which would mean it didn't parse correctly)

if len(df.columns) == 1:
    # It might be that the file is actually a CSV inside a single column or has weird quoting.
    # Let's try to reload with specific parameters if needed.
    # Re-reading using the first column as header if it's just one big string
    import csv
    df = pd.read_csv('supplychain project.csv', encoding='ISO-8859-1', quotechar='"', skipinitialspace=True)

print("Columns:", df.columns.tolist())
print("Shape:", df.shape)
print("Head:\n", df.head())
print("Data Types:\n", df.dtypes)

with open('supplychain project.csv', 'r', encoding='ISO-8859-1') as f:
    for i in range(5):
        print(repr(f.readline()))

import pandas as pd
import io

# Step 2: Correctly read the strangely formatted CSV

with open('supplychain project.csv', 'r', encoding='ISO-8859-1') as f:
    cleaned_lines = [line.strip().strip('"') for line in f]

df = pd.read_csv(io.StringIO('\n'.join(cleaned_lines)))

# Initial check
print("Shape before cleaning:", df.shape)

# Define key columns for supply chain optimization
key_columns = ['Order_id', 'Order_Date', 'Shipping_Date', 'Product_Category', 
               'Cust_City', 'Cust_Country', 'Qnty', 'Sales', 'Profit', 'Cost']

# 1. Handling missing values in key columns
# Check missing values
print("Missing values in key columns:\n", df[key_columns].isnull().sum())
# Strategy: drop rows where key columns are missing
df = df.dropna(subset=key_columns)

# 2. Remove duplicate rows
df = df.drop_duplicates()

# 3. Standardize cost and profit units to numeric
df['Cost'] = pd.to_numeric(df['Cost'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
# Also ensure Sales and Qnty are numeric
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Qnty'] = pd.to_numeric(df['Qnty'], errors='coerce')

# Drop any rows where numeric conversion failed for essential metrics
df = df.dropna(subset=['Cost', 'Profit', 'Sales', 'Qnty'])

# 4. Creating a new column for shipping_delay = Shipping_Date - Order_Date
# Convert date columns to datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Shipping_Date'] = pd.to_datetime(df['Shipping_Date'])

# Calculate delay in days
df['shipping_delay'] = (df['Shipping_Date'] - df['Order_Date']).dt.days

# Final check
print("Shape after cleaning:", df.shape)
print("Cleaned Data Head:\n", df[['Order_Date', 'Shipping_Date', 'shipping_delay', 'Profit', 'Cost']].head())

# Save the cleaned dataset
df.to_csv('cleaned_supplychain_dataset.csv', index=False)