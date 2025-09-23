import streamlit as st
import pandas as pd
import numpy as np

def show_content(df):
    st.markdown('<h2 class="tab-header">🔍 Slicing and Indexing DataFrames</h2>', unsafe_allow_html=True)
    
    # Explicit indexes
    st.markdown("## Explicit Indexes")
    st.markdown("""
    Setting explicit indexes can make data access more intuitive and efficient, especially when you have meaningful row identifiers.
    """)
    
    # Setting and removing indexes
    st.markdown("### Setting and removing indexes")
    code = '''
# Set Date as index
df_date_index = df.set_index('Date')
print("DataFrame with Date as index:")
df_date_index.head()
'''
    st.code(code, language="python")
    df_date_index = df.set_index('Date')
    st.write("**Output:**")
    st.dataframe(df_date_index.head())
    
    code = '''
# Reset index back to default
df_reset = df_date_index.reset_index()
print("DataFrame with reset index:")
df_reset.head()
'''
    st.code(code, language="python")
    df_reset = df_date_index.reset_index()
    st.write("**Output:**")
    st.dataframe(df_reset.head())
    
    # Subsetting with .loc[]
    st.markdown("### Subsetting with .loc[]")
    code = '''
# Use .loc[] for label-based selection
print("Sales data for first date:")
first_date = df_date_index.index[0]
print(f"Date: {first_date}")
print(df_date_index.loc[first_date])
'''
    st.code(code, language="python")
    first_date = df_date_index.index[0]
    st.write("**Output:**")
    st.write(f"**Date:** {first_date}")
    result = df_date_index.loc[first_date]
    for idx, val in result.items():
        st.write(f"**{idx}:** {val}")
    
    # Setting multi-level indexes
    st.markdown("### Setting multi-level indexes")
    code = '''
# Create multi-level index
df_multi = df.set_index(['Store', 'Date'])
print("DataFrame with multi-level index:")
df_multi.head()
'''
    st.code(code, language="python")
    df_multi = df.set_index(['Store', 'Date'])
    st.write("**Output:**")
    st.dataframe(df_multi.head())
    
    # Sorting by index values
    st.markdown("### Sorting by index values")
    code = '''
# Sort by index
df_sorted_index = df_multi.sort_index()
print("DataFrame sorted by multi-level index:")
df_sorted_index.head()
'''
    st.code(code, language="python")
    df_sorted_index = df_multi.sort_index()
    st.write("**Output:**")
    st.dataframe(df_sorted_index.head())
    
    # Slicing and subsetting with .loc and .iloc
    st.markdown("## Slicing and subsetting with .loc and .iloc")
    
    # Slicing index values
    st.markdown("### Slicing index values")
    code = '''
# Slice by date range using .loc[]
start_date = df_date_index.index[5]
end_date = df_date_index.index[15]
date_slice = df_date_index.loc[start_date:end_date]
print(f"Data from {start_date} to {end_date}:")
date_slice.head()
'''
    st.code(code, language="python")
    start_date = df_date_index.index[5]
    end_date = df_date_index.index[15]
    date_slice = df_date_index.loc[start_date:end_date]
    st.write("**Output:**")
    st.write(f"Data from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}:")
    st.dataframe(date_slice.head())
    
    # Slicing in both directions
    st.markdown("### Slicing in both directions")
    code = '''
# Slice rows and columns simultaneously
subset = df_date_index.loc[start_date:end_date, ['Store', 'Sales']]
print("Subset with specific date range and columns:")
subset.head()
'''
    st.code(code, language="python")
    subset = df_date_index.loc[start_date:end_date, ['Store', 'Sales']]
    st.write("**Output:**")
    st.dataframe(subset.head())
    
    # Slicing time series
    st.markdown("### Slicing time series")
    code = '''
# Advanced time-based slicing
df_time = df.set_index('Date')
# Get data for specific month
january_data = df_time.loc['2024-01']
print(f"January 2024 data ({len(january_data)} records):")
january_data.head()
'''
    st.code(code, language="python")
    df_time = df.set_index('Date')
    january_data = df_time.loc['2024-01']
    st.write("**Output:**")
    st.write(f"January 2024 data ({len(january_data)} records):")
    st.dataframe(january_data.head())
    
    # Subsetting by row/column number
    st.markdown("### Subsetting by row/column number")
    code = '''
# Use .iloc[] for position-based selection
print("First 5 rows and first 3 columns:")
subset_iloc = df.iloc[:5, :3]
subset_iloc
'''
    st.code(code, language="python")
    subset_iloc = df.iloc[:5, :3]
    st.write("**Output:**")
    st.dataframe(subset_iloc)
    
    code = '''
# Select specific rows and columns by position
print("Rows 10-15, columns 1-3:")
specific_subset = df.iloc[10:15, 1:4]
specific_subset
'''
    st.code(code, language="python")
    specific_subset = df.iloc[10:15, 1:4]
    st.write("**Output:**")
    st.dataframe(specific_subset)
    
    # Working with pivot tables
    st.markdown("## Working with pivot tables")
    
    # Pivot temperature by city and year
    st.markdown("### Pivot sales by store and month")
    code = '''
# Create pivot table for analysis
df_analysis = df.copy()
df_analysis['Month'] = df_analysis['Date'].dt.month
df_analysis['Week'] = df_analysis['Date'].dt.isocalendar().week

pivot_sales = df_analysis.pivot_table(
    values='Sales',
    index='Store',
    columns='Month',
    aggfunc='mean',
    fill_value=0
).round(2)
print("Sales by Store and Month:")
pivot_sales
'''
    st.code(code, language="python")
    df_analysis = df.copy()
    df_analysis['Month'] = df_analysis['Date'].dt.month
    df_analysis['Week'] = df_analysis['Date'].dt.isocalendar().week
    pivot_sales = df_analysis.pivot_table(
        values='Sales',
        index='Store',
        columns='Month',
        aggfunc='mean',
        fill_value=0
    ).round(2)
    st.write("**Output:**")
    st.dataframe(pivot_sales)
    
    # Subsetting pivot tables
    st.markdown("### Subsetting pivot tables")
    code = '''
# Select specific stores from pivot table
selected_stores = ['Store_A', 'Store_B']
pivot_subset = pivot_sales.loc[selected_stores]
print("Pivot table for Store A and B only:")
pivot_subset
'''
    st.code(code, language="python")
    selected_stores = ['Store_A', 'Store_B']
    pivot_subset = pivot_sales.loc[selected_stores]
    st.write("**Output:**")
    st.dataframe(pivot_subset)
    
    # Calculating on a pivot table
    st.markdown("### Calculating on a pivot table")
    code = '''
# Perform calculations on pivot table
pivot_with_totals = pivot_sales.copy()
pivot_with_totals['Total'] = pivot_with_totals.sum(axis=1)
pivot_with_totals.loc['Average'] = pivot_with_totals.mean()

print("Pivot table with totals and averages:")
pivot_with_totals.round(2)
'''
    st.code(code, language="python")
    pivot_with_totals = pivot_sales.copy()
    pivot_with_totals['Total'] = pivot_with_totals.sum(axis=1)
    pivot_with_totals.loc['Average'] = pivot_with_totals.mean()
    st.write("**Output:**")
    st.dataframe(pivot_with_totals.round(2))
    
    # Advanced indexing examples
    st.markdown("## Advanced Indexing Examples")
    code = '''
# Boolean indexing with multiple conditions
high_sales_store_a = df[(df['Sales'] > 3000) & (df['Store'] == 'Store_A')]
print(f"Store A with high sales: {len(high_sales_store_a)} records")
high_sales_store_a
'''
    st.code(code, language="python")
    high_sales_store_a = df[(df['Sales'] > 3000) & (df['Store'] == 'Store_A')]
    st.write("**Output:**")
    st.write(f"Store A with high sales: {len(high_sales_store_a)} records")
    st.dataframe(high_sales_store_a)
    
    code = '''
# Query method for complex filtering
query_result = df.query('Sales > 3000 and Customers > 100')
print(f"Query result: {len(query_result)} records")
query_result.head()
'''
    st.code(code, language="python")
    query_result = df.query('Sales > 3000 and Customers > 100')
    st.write("**Output:**")
    st.write(f"Query result: {len(query_result)} records")
    st.dataframe(query_result.head())