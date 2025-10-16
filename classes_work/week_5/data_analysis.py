import numpy as np
import pandas as pd

# 1. Create data with NumPy
print("--- Step 1: Creating a NumPy array ---")
# Create a 2D NumPy array representing sales data for 3 stores over 5 days
sales_data = np.array([
    [150, 200, 180, 220, 190],
    [160, 190, 210, 200, 230],
    [170, 180, 175, 190, 200]
])
print("Original NumPy array (sales_data):")
print(sales_data)
print("-" * 40)

# 2. Perform operations with NumPy
print("--- Step 2: Performing NumPy operations ---")
# Calculate the total sales for all stores
total_sales = np.sum(sales_data)
print(f"Total sales for all stores: {total_sales}")

# Calculate the average daily sales for each store
avg_sales_per_store = np.mean(sales_data, axis=1)
print("Average daily sales per store:")
print(avg_sales_per_store)

# Find the maximum sales value across all data points
max_sales = np.max(sales_data)
print(f"Highest single day sales: {max_sales}")
print("-" * 40)

# 3. Create a DataFrame with Pandas
print("--- Step 3: Creating a Pandas DataFrame ---")
# Create a DataFrame from the NumPy array with labels
df = pd.DataFrame(
    sales_data,
    index=['Store A', 'Store B', 'Store C'],
    columns=['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
)
print("Pandas DataFrame:")
print(df)
print("-" * 40)

# 4. Perform analysis with Pandas
print("--- Step 4: Performing Pandas analysis ---")
# Get descriptive statistics for the data
print("Descriptive statistics:")
print(df.describe())
print("\n" + "-" * 40)

# Select a specific row (store)
store_b_sales = df.loc['Store B']
print("Sales data for Store B:")
print(store_b_sales)
print("\n" + "-" * 40)

# Add a new column for total sales per store
df['Total Sales'] = df.sum(axis=1)
print("DataFrame with new 'Total Sales' column:")
print(df)
print("\n" + "-" * 40)

# Filter data to find stores with total sales over 1000
high_performing_stores = df[df['Total Sales'] > 1000]
print("High-performing stores (total sales > 1000):")
print(high_performing_stores)

## by default iloc uses zero-based indexing iloc[row_index, column_index]
print(df.iloc[0])  # First row
print(df.iloc[:, 0])  # First column
print(df.iloc[0, 0])  # First element
print(df)


print(df.iloc[1,3])  # Second row, fourth column

#Solution 2: Use .loc[] for label-based selection
print(df.loc['Store B', 'Day 1':'Day 3'])
