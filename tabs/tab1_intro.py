import streamlit as st
import pandas as pd

def show_content(df):
    st.markdown('<h2 class="tab-header">🚀 Intro to Data Manipulation with Pandas</h2>', unsafe_allow_html=True)
    
    # Introducing DataFrames
    st.markdown("## Introducing DataFrames")
    st.markdown("""
    A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. 
    You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
    """)
    
    code = '''
# Display the first few rows of our dataset
print("First 5 rows of the dataset:")
df.head()
'''
    st.code(code, language="python")
    st.write("**Output:**")
    st.dataframe(df.head())
    
    # Inspecting a DataFrame
    st.markdown("## Inspecting a DataFrame")
    st.markdown("""
    Before working with data, it's important to understand its structure, data types, and basic statistics.
    """)
    
    code = '''
# Basic information about the DataFrame
print("DataFrame Info:")
df.info()
print("\\nDataFrame Shape:", df.shape)
print("\\nData Types:")
df.dtypes
'''
    st.code(code, language="python")
    st.write("**Output:**")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**DataFrame Shape:**", df.shape)
        st.write("**Data Types:**")
        st.write(df.dtypes)
    with col2:
        st.write("**Basic Statistics:**")
        st.dataframe(df.describe())
    
    # Parts of a DataFrame
    st.markdown("## Parts of a DataFrame")
    st.markdown("""
    A DataFrame consists of three main components: the index (row labels), columns (column labels), and values (the actual data).
    """)
    
    code = '''
# Access different parts of the DataFrame
print("Column names:", df.columns.tolist())
print("Index:", df.index.tolist()[:10], "...")  # Show first 10
print("Values shape:", df.values.shape)
'''
    st.code(code, language="python")
    st.write("**Output:**")
    st.write("**Column names:**", df.columns.tolist())
    st.write("**Index (first 10):**", df.index.tolist()[:10])
    st.write("**Values shape:**", df.values.shape)
    
    # Sorting and subsetting
    st.markdown("## Sorting and Subsetting")
    st.markdown("""
    Sorting and subsetting are fundamental operations for data analysis. They help you organize and focus on specific parts of your data.
    """)
    
    # Sorting rows
    st.markdown("### Sorting Rows")
    code = '''
# Sort by Sales column in descending order
df_sorted = df.sort_values('Sales', ascending=False)
print("Top 5 sales days:")
df_sorted.head()
'''
    st.code(code, language="python")
    df_sorted = df.sort_values('Sales', ascending=False)
    st.write("**Output:**")
    st.dataframe(df_sorted.head())
    
    # Subsetting columns
    st.markdown("### Subsetting Columns")
    code = '''
# Select specific columns
sales_data = df[['Date', 'Sales']]
print("Sales data only:")
sales_data.head()
'''
    st.code(code, language="python")
    sales_data = df[['Date', 'Sales']]
    st.write("**Output:**")
    st.dataframe(sales_data.head())
    
    # Subsetting rows
    st.markdown("### Subsetting Rows")
    code = '''
# Filter rows where Sales > 3000
high_sales = df[df['Sales'] > 3000]
print(f"Days with sales > $3000: {len(high_sales)} out of {len(df)}")
high_sales.head()
'''
    st.code(code, language="python")
    high_sales = df[df['Sales'] > 3000]
    st.write("**Output:**")
    st.write(f"Days with sales > $3000: {len(high_sales)} out of {len(df)}")
    st.dataframe(high_sales.head())
    
    # Subsetting rows by categorical variables
    st.markdown("### Subsetting Rows by Categorical Variables")
    code = '''
# Filter by store type
store_a_data = df[df['Store'] == 'Store_A']
print(f"Store A data: {len(store_a_data)} records")
store_a_data.head()
'''
    st.code(code, language="python")
    store_a_data = df[df['Store'] == 'Store_A']
    st.write("**Output:**")
    st.write(f"Store A data: {len(store_a_data)} records")
    st.dataframe(store_a_data.head())
    
    # New columns
    st.markdown("## New Columns")
    st.markdown("""
    Creating new columns is a powerful way to derive insights from existing data.
    """)
    
    # Adding new columns
    st.markdown("### Adding New Columns")
    code = '''
# Create new columns based on existing data
df_new = df.copy()
df_new['Sales_per_Customer'] = df_new['Sales'] / df_new['Customers']
df_new['Month'] = df_new['Date'].dt.month
df_new['Weekday'] = df_new['Date'].dt.day_name()

print("DataFrame with new columns:")
df_new[['Date', 'Store', 'Sales', 'Customers', 'Sales_per_Customer', 'Month', 'Weekday']].head()
'''
    st.code(code, language="python")
    df_new = df.copy()
    df_new['Sales_per_Customer'] = df_new['Sales'] / df_new['Customers']
    df_new['Month'] = df_new['Date'].dt.month
    df_new['Weekday'] = df_new['Date'].dt.day_name()
    st.write("**Output:**")
    st.dataframe(df_new[['Date', 'Store', 'Sales', 'Customers', 'Sales_per_Customer', 'Month', 'Weekday']].head())