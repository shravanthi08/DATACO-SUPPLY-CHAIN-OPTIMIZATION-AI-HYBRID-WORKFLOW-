# Visualization 
# Line Chart showing profit trends over time 

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Ensure Order_Date is datetime
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Sort by date
df = df.sort_values('Order_Date')

# Grouping by Month
df['Month_Year'] = df['Order_Date'].dt.to_period('M')
monthly_profit = df.groupby('Month_Year')['Profit'].sum().reset_index()
monthly_profit['Month_Year'] = monthly_profit['Month_Year'].dt.to_timestamp()

# Grouping by Quarter
df['Quarter_Year'] = df['Order_Date'].dt.to_period('Q')
quarterly_profit = df.groupby('Quarter_Year')['Profit'].sum().reset_index()
quarterly_profit['Quarter_Year'] = quarterly_profit['Quarter_Year'].dt.to_timestamp()

# Visualization: Line Chart for Profit Trends (Monthly)

plt.figure(figsize=(14, 7))
plt.plot(monthly_profit['Month_Year'], monthly_profit['Profit'], marker='o', linestyle='-', color='#1f77b4', label='Monthly Profit')
plt.plot(quarterly_profit['Quarter_Year'], quarterly_profit['Profit'] / 3, marker='s', linestyle='--', color='#ff7f0e', label='Quarterly Average (Monthly scale)')

plt.title('Profit Trends Over Time: Identifying Seasonality', fontsize=16)
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Profit ($)', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.7)
plt.tight_layout()
plt.savefig('profit_seasonal_trends.png')

# Save the trend data
monthly_profit.to_csv('monthly_profit_trend.csv', index=False)
quarterly_profit.to_csv('quarterly_profit_trend.csv', index=False)

# Display head/tail to check patterns
print("Monthly Profit Trend (Recent Months):")
print(monthly_profit.tail())

# Visualization
# Heatmap of average shipping delays by country 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Check columns and counts
print("Unique Order Regions:", df['Order Region'].nunique())
print("Unique Shipping Modes:", df['Shipping Mode'].nunique())

# Create a pivot table for the heatmap: Order Region vs Shipping Mode
# This highlights which combinations are "bottlenecks"
heatmap_data = df.pivot_table(index='Order Region', columns='Shipping Mode', values='shipping_delay', aggfunc='mean')

# Plotting the heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(heatmap_data, annot=True, cmap='YlOrRd', fmt='.2f', cbar_kws={'label': 'Avg Shipping Delay (Days)'})

plt.title('Heatmap of Average Shipping Delays by Region and Mode', fontsize=16)
plt.xlabel('Shipping Mode', fontsize=12)
plt.ylabel('Order Region', fontsize=12)
plt.tight_layout()
plt.savefig('shipping_delay_heatmap.png')

# Save the heatmap data for the user
heatmap_data.to_csv('shipping_delay_heatmap_data.csv')

# Visualization 
# cost vs sales comparison (Scatter Plot)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Visualization: Scatter Plot Cost vs Sales
plt.figure(figsize=(10, 8))
sns.scatterplot(data=df, x='Cost', y='Sales', alpha=0.3, color='purple', edgecolor=None)

# Adding a 1:1 reference line (where Sales = Cost)
max_val = max(df['Cost'].max(), df['Sales'].max())
plt.plot([0, max_val], [0, max_val], 'r--', label='Break-even line (Sales=Cost)')

plt.title('Cost vs Sales Analysis: Detecting Efficiency and Outliers', fontsize=16)
plt.xlabel('Cost (Unit/Production Cost)', fontsize=12)
plt.ylabel('Sales (Revenue per Order)', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.tight_layout()
plt.savefig('cost_vs_sales_scatter.png')

# Statistical correlation
correlation = df['Cost'].corr(df['Sales'])
print(f"Correlation between Cost and Sales: {correlation:.4f}")

# visualization 4:
# Top Customer by sales (Barchart)

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Look for customer name columns
# Based on the original structure, they were 'Customer Fname' and 'Customer Lname'
# Let's verify columns first
print("Columns in dataset:", df.columns.tolist())

# Combine First and Last names for the chart labels
# We'll use 'Customer Id' as the primary key just in case names are duplicated
df['Customer_Full_Name'] = df['Customer Fname'].astype(str) + ' ' + df['Customer Lname'].astype(str)

# Group by Customer Id and Name, then sum Sales
customer_sales = df.groupby(['Customer Id', 'Customer_Full_Name'])['Sales'].sum().reset_index()

# Sort and get the top 10
top_10_customers = customer_sales.sort_values(by='Sales', ascending=False).head(10)

# Create the Bar Chart
plt.figure(figsize=(12, 8))
plt.barh(top_10_customers['Customer_Full_Name'], top_10_customers['Sales'], color='darkblue')
plt.xlabel('Total Sales ($)', fontsize=12)
plt.ylabel('Customer Name', fontsize=12)
plt.title('Top 10 Customers by Total Sales (Key Accounts)', fontsize=16)
plt.gca().invert_yaxis()  # Put the highest sales at the top
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('top_10_customers_sales.png')

# Save the top 10 list
top_10_customers.to_csv('top_10_customers_summary.csv', index=False)

print("Top 10 Customers by Sales:")
print(top_10_customers[['Customer_Full_Name', 'Sales']])

# visualization 5
# profit margin analysis (Box Plot)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Calculate Profit Margin
# Avoid division by zero
df['Profit_Margin'] = df['Profit'] / df['Sales'].replace(0, float('nan'))

# Get top 15 categories by order frequency to keep the plot readable
top_categories = df['Product_Category'].value_counts().nlargest(15).index
df_filtered = df[df['Product_Category'].isin(top_categories)]

# Create the Boxplot
plt.figure(figsize=(14, 8))
sns.boxplot(data=df_filtered, x='Product_Category', y='Profit_Margin', palette='Set3')

plt.title('Distribution of Profit Margins across Top 15 Product Categories', fontsize=16)
plt.xlabel('Product Category', fontsize=12)
plt.ylabel('Profit Margin (Profit/Sales)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('profit_margin_boxplot.png')

# Statistical summary of profit margins for these categories
margin_stats = df_filtered.groupby('Product_Category')['Profit_Margin'].describe()
margin_stats.to_csv('profit_margin_statistics.csv')

print("Profit Margin Stats (First 5 categories):")
print(margin_stats.head())

