import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta

def show_content(df):
    st.markdown('<h2 class="tab-header">📈 Creating and Visualizing DataFrames</h2>', unsafe_allow_html=True)
    
    # Visualizing your data
    st.markdown("## Visualizing your data")
    st.markdown("""
    Data visualization is crucial for understanding patterns, trends, and insights in your data. Let's explore various ways to visualize our sales data.
    """)
    
    # Which store type is most popular?
    st.markdown("### Which store type is most popular?")
    code = '''
# Create bar plot for store popularity
import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(10, 6))
store_counts = df['Store'].value_counts()
plt.bar(store_counts.index, store_counts.values)
plt.title('Number of Sales Records by Store')
plt.xlabel('Store')
plt.ylabel('Number of Records')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
'''
    st.code(code, language="python")
    st.write("**Output:**")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    store_counts = df['Store'].value_counts()
    ax.bar(store_counts.index, store_counts.values, color='skyblue')
    ax.set_title('Number of Sales Records by Store')
    ax.set_xlabel('Store')
    ax.set_ylabel('Number of Records')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Changes in sales over time
    st.markdown("### Changes in sales over time")
    code = '''
# Line plot for sales over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Sales'], marker='o', linewidth=2, markersize=4)
plt.title('Sales Over Time')
plt.xlabel('Date')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
'''
    st.code(code, language="python")
    st.write("**Output:**")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['Date'], df['Sales'], marker='o', linewidth=2, markersize=4, color='green')
    ax.set_title('Sales Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales ($)')
    plt.xticks(rotation=45)
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Store performance comparison
    st.markdown("### Store performance comparison")
    code = '''
# Box plot for sales distribution by store
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Store', y='Sales')
plt.title('Sales Distribution by Store')
plt.xlabel('Store')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
'''
    st.code(code, language="python")
    st.write("**Output:**")
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.boxplot(data=df, x='Store', y='Sales', ax=ax)
    ax.set_title('Sales Distribution by Store')
    ax.set_xlabel('Store')
    ax.set_ylabel('Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Sales vs Customers relationship
    st.markdown("### Sales vs Customers relationship")
    code = '''
# Scatter plot for relationship analysis
plt.figure(figsize=(10, 6))
colors = {'Store_A': 'red', 'Store_B': 'blue', 'Store_C': 'green', 
          'Store_D': 'orange', 'Store_E': 'purple'}
for store in df['Store'].unique():
    store_data = df[df['Store'] == store]
    plt.scatter(store_data['Customers'], store_data['Sales'], 
                label=store, alpha=0.7, color=colors[store])

plt.title('Sales vs Customers by Store')
plt.xlabel('Number of Customers')
plt.ylabel('Sales ($)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
'''
    st.code(code, language="python")
    st.write("**Output:**")
    
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = {'Store_A': 'red', 'Store_B': 'blue', 'Store_C': 'green', 
              'Store_D': 'orange', 'Store_E': 'purple'}
    for store in df['Store'].unique():
        store_data = df[df['Store'] == store]
        ax.scatter(store_data['Customers'], store_data['Sales'], 
                  label=store, alpha=0.7, color=colors[store])
    
    ax.set_title('Sales vs Customers by Store')
    ax.set_xlabel('Number of Customers')
    ax.set_ylabel('Sales ($)')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Missing values
    st.markdown("## Missing values")
    st.markdown("""
    Real-world data often contains missing values. Let's learn how to detect, handle, and replace them.
    """)
    
    # Finding missing values
    st.markdown("### Finding missing values")
    code = '''
# Check for missing values
print("Missing values in each column:")
missing_values = df.isnull().sum()
print(missing_values)
print(f"\\nTotal missing values: {df.isnull().sum().sum()}")

# Percentage of missing values
missing_percentage = (df.isnull().sum() / len(df) * 100).round(2)
print("\\nPercentage of missing values:")
print(missing_percentage)
'''
    st.code(code, language="python")
    st.write("**Output:**")
    missing_values = df.isnull().sum()
    st.write("**Missing values in each column:**")
    st.write(missing_values)
    st.write(f"**Total missing values:** {df.isnull().sum().sum()}")
    
    # Create sample data with missing values for demonstration
    st.markdown("### Creating sample data with missing values")
    code = '''
# Create a copy with some artificial missing values for demonstration
df_with_missing = df.copy()
# Randomly set some values to NaN
np.random.seed(42)
missing_indices = np.random.choice(df_with_missing.index, size=10, replace=False)
df_with_missing.loc[missing_indices[:5], 'Sales'] = np.nan
df_with_missing.loc[missing_indices[5:], 'Customers'] = np.nan

print("Missing values in modified dataset:")
print(df_with_missing.isnull().sum())
'''
    st.code(code, language="python")
    df_with_missing = df.copy()
    np.random.seed(42)
    missing_indices = np.random.choice(df_with_missing.index, size=10, replace=False)
    df_with_missing.loc[missing_indices[:5], 'Sales'] = np.nan
    df_with_missing.loc[missing_indices[5:], 'Customers'] = np.nan
    st.write("**Output:**")
    st.write("Missing values in modified dataset:")
    st.write(df_with_missing.isnull().sum())
    
    # Removing missing values
    st.markdown("### Removing missing values")
    code = '''
# Remove rows with any missing values
df_no_missing = df_with_missing.dropna()
print(f"Original shape: {df_with_missing.shape}")
print(f"After removing missing values: {df_no_missing.shape}")
print(f"Rows removed: {len(df_with_missing) - len(df_no_missing)}")
'''
    st.code(code, language="python")
    df_no_missing = df_with_missing.dropna()
    st.write("**Output:**")
    st.write(f"**Original shape:** {df_with_missing.shape}")
    st.write(f"**After removing missing values:** {df_no_missing.shape}")
    st.write(f"**Rows removed:** {len(df_with_missing) - len(df_no_missing)}")
    
    # Replacing missing values
    st.markdown("### Replacing missing values")
    code = '''
# Fill missing values with different strategies
df_filled = df_with_missing.copy()

# Fill Sales with mean
df_filled['Sales'] = df_filled['Sales'].fillna(df_filled['Sales'].mean())

# Fill Customers with median
df_filled['Customers'] = df_filled['Customers'].fillna(df_filled['Customers'].median())

print("After filling missing values:")
print(df_filled.isnull().sum())
print("\\nFirst few rows of filled data:")
df_filled.head()
'''
    st.code(code, language="python")
    df_filled = df_with_missing.copy()
    df_filled['Sales'] = df_filled['Sales'].fillna(df_filled['Sales'].mean())
    df_filled['Customers'] = df_filled['Customers'].fillna(df_filled['Customers'].median())
    st.write("**Output:**")
    st.write("After filling missing values:")
    st.write(df_filled.isnull().sum())
    st.write("First few rows of filled data:")
    st.dataframe(df_filled.head())
    
    # Creating DataFrames
    st.markdown("## Creating DataFrames")
    st.markdown("""
    There are several ways to create DataFrames from different data structures. Let's explore the most common methods.
    """)
    
    # List of dictionaries
    st.markdown("### List of dictionaries")
    code = '''
# Create DataFrame from list of dictionaries
data_list = [
    {'Product': 'A', 'Price': 10.99, 'Quantity': 100},
    {'Product': 'B', 'Price': 15.50, 'Quantity': 75},
    {'Product': 'C', 'Price': 8.25, 'Quantity': 150},
    {'Product': 'D', 'Price': 12.00, 'Quantity': 90}
]

df_from_list = pd.DataFrame(data_list)
print("DataFrame from list of dictionaries:")
df_from_list
'''
    st.code(code, language="python")
    data_list = [
        {'Product': 'A', 'Price': 10.99, 'Quantity': 100},
        {'Product': 'B', 'Price': 15.50, 'Quantity': 75},
        {'Product': 'C', 'Price': 8.25, 'Quantity': 150},
        {'Product': 'D', 'Price': 12.00, 'Quantity': 90}
    ]
    df_from_list = pd.DataFrame(data_list)
    st.write("**Output:**")
    st.dataframe(df_from_list)
    
    # Dictionary of lists
    st.markdown("### Dictionary of lists")
    code = '''
# Create DataFrame from dictionary of lists
data_dict = {
    'Product': ['A', 'B', 'C', 'D'],
    'Price': [10.99, 15.50, 8.25, 12.00],
    'Quantity': [100, 75, 150, 90],
    'Category': ['Electronics', 'Clothing', 'Books', 'Electronics']
}

df_from_dict = pd.DataFrame(data_dict)
print("DataFrame from dictionary of lists:")
df_from_dict
'''
    st.code(code, language="python")
    data_dict = {
        'Product': ['A', 'B', 'C', 'D'],
        'Price': [10.99, 15.50, 8.25, 12.00],
        'Quantity': [100, 75, 150, 90],
        'Category': ['Electronics', 'Clothing', 'Books', 'Electronics']
    }
    df_from_dict = pd.DataFrame(data_dict)
    st.write("**Output:**")
    st.dataframe(df_from_dict)
    
    # Reading and writing CSVs
    st.markdown("## Reading and writing CSVs")
    
    # CSV to DataFrame
    st.markdown("### CSV to DataFrame")
    code = '''
# Reading CSV files (example code)
# df_from_csv = pd.read_csv('sales_data.csv')
# print("DataFrame loaded from CSV:")
# print(df_from_csv.head())

# For demonstration, let's show the structure
print("Example of reading CSV:")
print("df = pd.read_csv('filename.csv')")
print("df.head()  # Display first 5 rows")
'''
    st.code(code, language="python")
    st.write("**Output (Example):**")
    st.write("This would load data from a CSV file into a DataFrame")
    st.write("Common parameters: sep, header, index_col, parse_dates")
    
    # DataFrame to CSV
    st.markdown("### DataFrame to CSV")
    code = '''
# Save DataFrame to CSV
csv_string = df.to_csv(index=False)
print("DataFrame saved to CSV format:")
print("First few lines of CSV:")
print(csv_string.split('\\n')[:6])  # Show first 6 lines

# Save to file (example)
# df.to_csv('output_sales_data.csv', index=False)
print("\\nTo save to file: df.to_csv('filename.csv', index=False)")
'''
    st.code(code, language="python")
    csv_string = df.to_csv(index=False)
    st.write("**Output:**")
    st.write("First few lines of CSV:")
    csv_lines = csv_string.split('\n')[:6]
    for line in csv_lines:
        if line:  # Skip empty lines
            st.code(line)
    st.write("To save to file: `df.to_csv('filename.csv', index=False)`")
    
    # Advanced DataFrame operations
    st.markdown("## Advanced DataFrame operations")
    code = '''
# Combine multiple operations
result = (df.groupby('Store')
          .agg({'Sales': ['mean', 'sum'], 'Customers': 'mean'})
          .round(2))

result.columns = ['Avg_Sales', 'Total_Sales', 'Avg_Customers']
result = result.sort_values('Total_Sales', ascending=False)

print("Advanced aggregation result:")
result
'''
    st.code(code, language="python")
    result = (df.groupby('Store')
              .agg({'Sales': ['mean', 'sum'], 'Customers': 'mean'})
              .round(2))
    result.columns = ['Avg_Sales', 'Total_Sales', 'Avg_Customers']
    result = result.sort_values('Total_Sales', ascending=False)
    st.write("**Output:**")
    st.dataframe(result)
    
    # Summary visualization
    st.markdown("### Summary Dashboard")
    code = '''
# Create a summary dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Sales distribution
axes[0,0].hist(df['Sales'], bins=15, alpha=0.7, color='skyblue')
axes[0,0].set_title('Sales Distribution')
axes[0,0].set_xlabel('Sales ($)')

# Sales by Store
store_sales = df.groupby('Store')['Sales'].mean()
axes[0,1].bar(store_sales.index, store_sales.values, color='lightgreen')
axes[0,1].set_title('Average Sales by Store')
axes[0,1].set_xlabel('Store')
axes[0,1].tick_params(axis='x', rotation=45)

# Sales over time
axes[1,0].plot(df['Date'], df['Sales'], color='orange', linewidth=2)
axes[1,0].set_title('Sales Trend Over Time')
axes[1,0].set_xlabel('Date')
axes[1,0].tick_params(axis='x', rotation=45)

# Customers vs Sales
axes[1,1].scatter(df['Customers'], df['Sales'], alpha=0.6, color='red')
axes[1,1].set_title('Sales vs Customers')
axes[1,1].set_xlabel('Customers')
axes[1,1].set_ylabel('Sales ($)')

plt.tight_layout()
plt.show()
'''
    st.code(code, language="python")
    st.write("**Output:**")
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Sales distribution
    axes[0,0].hist(df['Sales'], bins=15, alpha=0.7, color='skyblue')
    axes[0,0].set_title('Sales Distribution')
    axes[0,0].set_xlabel('Sales ($)')
    
    # Sales by Store
    store_sales = df.groupby('Store')['Sales'].mean()
    axes[0,1].bar(store_sales.index, store_sales.values, color='lightgreen')
    axes[0,1].set_title('Average Sales by Store')
    axes[0,1].set_xlabel('Store')
    axes[0,1].tick_params(axis='x', rotation=45)
    
    # Sales over time
    axes[1,0].plot(df['Date'], df['Sales'], color='orange', linewidth=2)
    axes[1,0].set_title('Sales Trend Over Time')
    axes[1,0].set_xlabel('Date')
    axes[1,0].tick_params(axis='x', rotation=45)
    
    # Customers vs Sales
    axes[1,1].scatter(df['Customers'], df['Sales'], alpha=0.6, color='red')
    axes[1,1].set_title('Sales vs Customers')
    axes[1,1].set_xlabel('Customers')
    axes[1,1].set_ylabel('Sales ($)')
    
    plt.tight_layout()
    st.pyplot(fig)