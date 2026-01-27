# Supply Chain Optimization 

import pandas as pd

df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Check unique shipping modes and if 'Cost' varies significantly by mode vs category
mode_analysis = df.groupby('Shipping Mode').agg({'Cost': 'mean', 'shipping_delay': 'mean', 'Profit': 'mean'}).reset_index()
print("Analysis by Shipping Mode:")
print(mode_analysis)

# Check unique categories and demand (quantity)
category_demand = df.groupby('Product_Category')['Qnty'].sum().reset_index()
print("\nCategory Demand Summary (First 5):")
print(category_demand.head())

# Look for specific shipping cost related columns if any
potential_shipping_cols = [col for col in df.columns if 'ship' in col.lower() or 'cost' in col.lower()]
print("\nPotential Cost/Shipping columns:", potential_shipping_cols)