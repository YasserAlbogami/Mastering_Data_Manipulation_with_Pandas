import streamlit as st
import pandas as pd
import numpy as np

def show_content(df):
    st.markdown('<h2 class="tab-header">📊 Aggregating DataFrames</h2>', unsafe_allow_html=True)
    
    # Summary statistics
    st.markdown("## Summary Statistics")
    st.markdown("""
    Summary statistics provide a quick overview of your data's central tendencies, spread, and distribution.
    """)
    
    code = '''
# Basic summary statistics
print("Summary statistics for all numeric columns:")
df.describe()
'''
    st.code(code, language="python")
    st.write("**Output:**")
    st.dataframe(df.describe())
    
    # Mean and median
    st.markdown("### Mean and Median")
    code = '''
# Calculate mean and median for specific columns
print("Sales Statistics:")
print(f"Mean Sales: ${df['Sales'].mean():.2f}")
print(f"Median Sales: ${df['Sales'].median():.2f}")
print(f"Mean Customers: {df['Customers'].mean():.0f}")
print(f"Median Customers: {df['Customers'].median():.0f}")
'''
    st.code(code, language="python")
    st.write("**Output:**")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Mean Sales", f"${df['Sales'].mean():.2f}")
        st.metric("Mean Customers", f"{df['Customers'].mean():.0f}")
    with col2:
        st.metric("Median Sales", f"${df['Sales'].median():.2f}")
        st.metric("Median Customers", f"{df['Customers'].median():.0f}")
    
    # Summarizing dates
    st.markdown("### Summarizing Dates")
    code = '''
# Date range and summary
print("Date Range Summary:")
print(f"Start Date: {df['Date'].min()}")
print(f"End Date: {df['Date'].max()}")
print(f"Total Days: {(df['Date'].max() - df['Date'].min()).days + 1}")
'''
    st.code(code, language="python")
    st.write("**Output:**")
    st.write(f"**Start Date:** {df['Date'].min().strftime('%Y-%m-%d')}")
    st.write(f"**End Date:** {df['Date'].max().strftime('%Y-%m-%d')}")
    st.write(f"**Total Days:** {(df['Date'].max() - df['Date'].min()).days + 1}")
    
    # Efficient summaries
    st.markdown("## Efficient Summaries")
    code = '''
# Multiple statistics at once using agg()
summary = df[['Sales', 'Customers']].agg(['mean', 'median', 'std', 'min', 'max'])
summary
'''
    st.code(code, language="python")
    summary = df[['Sales', 'Customers']].agg(['mean', 'median', 'std', 'min', 'max'])
    st.write("**Output:**")
    st.dataframe(summary)
    
    # Cumulative statistics
    st.markdown("### Cumulative Statistics")
    code = '''
# Calculate cumulative sum and rolling average
df_cum = df.copy()
df_cum['Cumulative_Sales'] = df_cum['Sales'].cumsum()
df_cum['Rolling_Avg_Sales'] = df_cum['Sales'].rolling(window=7).mean()
df_cum[['Date', 'Sales', 'Cumulative_Sales', 'Rolling_Avg_Sales']].head(10)
'''
    st.code(code, language="python")
    df_cum = df.copy()
    df_cum['Cumulative_Sales'] = df_cum['Sales'].cumsum()
    df_cum['Rolling_Avg_Sales'] = df_cum['Sales'].rolling(window=7).mean()
    st.write("**Output:**")
    st.dataframe(df_cum[['Date', 'Sales', 'Cumulative_Sales', 'Rolling_Avg_Sales']].head(10))
    
    # Counting
    st.markdown("## Counting")
    code = '''
# Count occurrences
print("Store counts:")
store_counts = df['Store'].value_counts()
print(store_counts)
'''
    st.code(code, language="python")
    store_counts = df['Store'].value_counts()
    st.write("**Output:**")
    st.dataframe(store_counts)
    
    # Dropping duplicates
    st.markdown("### Dropping Duplicates")
    code = '''
# Check for and remove duplicates
print(f"Original DataFrame shape: {df.shape}")
df_no_duplicates = df.drop_duplicates()
print(f"After removing duplicates: {df_no_duplicates.shape}")
print(f"Duplicates found: {len(df) - len(df_no_duplicates)}")
'''
    st.code(code, language="python")
    df_no_duplicates = df.drop_duplicates()
    st.write("**Output:**")
    st.write(f"**Original DataFrame shape:** {df.shape}")
    st.write(f"**After removing duplicates:** {df_no_duplicates.shape}")
    st.write(f"**Duplicates found:** {len(df) - len(df_no_duplicates)}")
    
    # Counting categorical variables
    st.markdown("### Counting Categorical Variables")
    code = '''
# Count and percentage of categorical variables
store_stats = df['Store'].value_counts()
store_percentage = df['Store'].value_counts(normalize=True) * 100

result = pd.DataFrame({
    'Count': store_stats,
    'Percentage': store_percentage.round(2)
})
result
'''
    st.code(code, language="python")
    store_stats = df['Store'].value_counts()
    store_percentage = df['Store'].value_counts(normalize=True) * 100
    result = pd.DataFrame({
        'Count': store_stats,
        'Percentage': store_percentage.round(2)
    })
    st.write("**Output:**")
    st.dataframe(result)
    
    # Grouped summary statistics
    st.markdown("## Grouped Summary Statistics")
    code = '''
# Group by store and calculate statistics
grouped_stats = df.groupby('Store').agg({
    'Sales': ['mean', 'sum', 'count'],
    'Customers': ['mean', 'sum']
}).round(2)
grouped_stats
'''
    st.code(code, language="python")
    grouped_stats = df.groupby('Store').agg({
        'Sales': ['mean', 'sum', 'count'],
        'Customers': ['mean', 'sum']
    }).round(2)
    st.write("**Output:**")
    st.dataframe(grouped_stats)
    
    # What percent of sales occurred at each store type?
    st.markdown("### What percent of sales occurred at each store type?")
    code = '''
# Calculate percentage of total sales by store
total_sales = df['Sales'].sum()
sales_by_store = df.groupby('Store')['Sales'].sum()
sales_percentage = (sales_by_store / total_sales * 100).round(2)

print("Percentage of sales by store:")
for store, pct in sales_percentage.items():
    print(f"{store}: {pct}%")
'''
    st.code(code, language="python")
    total_sales = df['Sales'].sum()
    sales_by_store = df.groupby('Store')['Sales'].sum()
    sales_percentage = (sales_by_store / total_sales * 100).round(2)
    st.write("**Output:**")
    for store, pct in sales_percentage.items():
        st.write(f"**{store}:** {pct}%")
    
    # Calculations with .groupby()
    st.markdown("### Calculations with .groupby()")
    code = '''
# Advanced groupby calculations
df_with_month = df.copy()
df_with_month['Month'] = df_with_month['Date'].dt.month

monthly_stats = df_with_month.groupby(['Store', 'Month']).agg({
    'Sales': 'mean',
    'Customers': 'mean'
}).round(2)
monthly_stats.head(10)
'''
    st.code(code, language="python")
    df_with_month = df.copy()
    df_with_month['Month'] = df_with_month['Date'].dt.month
    monthly_stats = df_with_month.groupby(['Store', 'Month']).agg({
        'Sales': 'mean',
        'Customers': 'mean'
    }).round(2)
    st.write("**Output:**")
    st.dataframe(monthly_stats.head(10))
    
    # Multiple grouped summaries
    st.markdown("### Multiple Grouped Summaries")
    code = '''
# Multiple aggregations in one operation
multi_agg = df.groupby('Store').agg({
    'Sales': ['count', 'mean', 'std', 'min', 'max'],
    'Customers': ['mean', 'std']
}).round(2)
multi_agg
'''
    st.code(code, language="python")
    multi_agg = df.groupby('Store').agg({
        'Sales': ['count', 'mean', 'std', 'min', 'max'],
        'Customers': ['mean', 'std']
    }).round(2)
    st.write("**Output:**")
    st.dataframe(multi_agg)
    
    # Pivot tables
    st.markdown("## Pivot Tables")
    st.markdown("### Pivoting on one variable")
    code = '''
# Create a simple pivot table
df_pivot_data = df.copy()
df_pivot_data['Month'] = df_pivot_data['Date'].dt.month
df_pivot_data['Week'] = df_pivot_data['Date'].dt.isocalendar().week

pivot_simple = df_pivot_data.pivot_table(
    values='Sales',
    index='Store',
    aggfunc='mean'
).round(2)
pivot_simple
'''
    st.code(code, language="python")
    df_pivot_data = df.copy()
    df_pivot_data['Month'] = df_pivot_data['Date'].dt.month
    df_pivot_data['Week'] = df_pivot_data['Date'].dt.isocalendar().week
    pivot_simple = df_pivot_data.pivot_table(
        values='Sales',
        index='Store',
        aggfunc='mean'
    ).round(2)
    st.write("**Output:**")
    st.dataframe(pivot_simple)
    
    # Fill in missing values and sum values with pivot tables
    st.markdown("### Fill in missing values and sum values with pivot tables")
    code = '''
# Pivot table with multiple dimensions
pivot_complex = df_pivot_data.pivot_table(
    values=['Sales', 'Customers'],
    index='Store',
    columns='Month',
    aggfunc='mean',
    fill_value=0
).round(2)
pivot_complex
'''
    st.code(code, language="python")
    pivot_complex = df_pivot_data.pivot_table(
        values=['Sales', 'Customers'],
        index='Store',
        columns='Month',
        aggfunc='mean',
        fill_value=0
    ).round(2)
    st.write("**Output:**")
    st.dataframe(pivot_complex)