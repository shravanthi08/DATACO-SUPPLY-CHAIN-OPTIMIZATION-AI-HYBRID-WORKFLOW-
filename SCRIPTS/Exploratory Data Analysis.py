# Step 3: Exploratory Data Analysis

# 1. Profit by Product Category

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Summarize total profit by product category
category_profit = df.groupby('Product_Category')['Profit'].sum().reset_index()

# Sort by profit for better visualization
category_profit = category_profit.sort_values(by='Profit', ascending=False)

# Display the summary table
print("Total Profit by Product Category:")
print(category_profit)

# Suggest and create a visualization: Horizontal Bar Chart
plt.figure(figsize=(12, 8))
plt.barh(category_profit['Product_Category'], category_profit['Profit'], color='skyblue')
plt.xlabel('Total Profit')
plt.ylabel('Product Category')
plt.title('Total Profit by Product Category')
plt.gca().invert_yaxis()  # Most profitable at the top
plt.tight_layout()
plt.savefig('profit_by_category.png')

# Save the summary to CSV as well
category_profit.to_csv('category_profit_summary.csv', index=False)

# 2. Shipping Delays by Country 

import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned dataset
df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Calculate average shipping delay by customer country
country_delay = df.groupby('Cust_Country')['shipping_delay'].mean().reset_index()
country_delay.columns = ['Customer Country', 'Average Shipping Delay']
country_delay = country_delay.sort_values(by='Average Shipping Delay', ascending=False)

# Calculate average shipping delay by order region (better for visualization/comparison)
region_delay = df.groupby('Order Region')['shipping_delay'].mean().reset_index()
region_delay.columns = ['Order Region', 'Average Shipping Delay']
region_delay = region_delay.sort_values(by='Average Shipping Delay', ascending=False)

# Display the summary for countries (top 10)
print("Average Shipping Delay by Customer Country (Top 10):")
print(country_delay.head(10))

# Suggest and create a visualization: Bar Chart for Regions
plt.figure(figsize=(12, 8))
plt.bar(region_delay['Order Region'], region_delay['Average Shipping Delay'], color='salmon')
plt.xlabel('Order Region')
plt.ylabel('Average Shipping Delay (Days)')
plt.title('Average Shipping Delay by Order Region')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('delay_by_region.png')

# Save results to CSV
country_delay.to_csv('average_delay_by_country.csv', index=False)
region_delay.to_csv('average_delay_by_region.csv', index=False)

# 3. Cost Distribution 

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset
df = pd.read_csv('cleaned_supplychain_dataset.csv')

# Descriptive statistics for Cost
cost_stats = df['Cost'].describe()
cost_skew = df['Cost'].skew()

print("Descriptive Statistics for Cost:")
print(cost_stats)
print(f"Skewness: {cost_skew}")

# Create visualizations
plt.figure(figsize=(14, 6))

# Histogram for skewness
plt.subplot(1, 2, 1)
sns.histplot(df['Cost'], kde=True, color='blue')
plt.title('Distribution of Cost (Histogram)')
plt.xlabel('Cost')
plt.ylabel('Frequency')

# Boxplot for outliers
plt.subplot(1, 2, 2)
sns.boxplot(x=df['Cost'], color='lightgreen')
plt.title('Detection of Outliers (Box Plot)')
plt.xlabel('Cost')

plt.tight_layout()
plt.savefig('cost_distribution_analysis.png')

# Re-save stats for reference if needed
cost_summary = pd.DataFrame(cost_stats).transpose()
cost_summary['skewness'] = cost_skew
cost_summary.to_csv('cost_distribution_summary.csv', index=False)

