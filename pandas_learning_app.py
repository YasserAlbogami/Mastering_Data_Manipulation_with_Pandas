import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns

# Import tab modules
from tabs import tab1_intro, tab2_aggregating, tab3_slicing, tab4_creating_viz

st.set_page_config(
    page_title="Data Manipulation with Pandas",
    page_icon="🐼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .tab-header {
        font-size: 2rem;
        color: #ff7f0e;
        margin-bottom: 1rem;
    }
    .section-header {
        font-size: 1.5rem;
        color: #2ca02c;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .code-block {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .download-section {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🐼 Data Manipulation with Pandas</h1>', unsafe_allow_html=True)

# Attribution
st.markdown(
    '<p style="text-align: center; margin: -10px 0 20px 0; color: #666;">Built by <a href="https://www.linkedin.com/in/yasser-albogami-650240291/" target="_blank" style="text-decoration: none; color: #0066cc;">Yasser A. Albogami</a></p>', 
    unsafe_allow_html=True
)

# Generate sample dataset
@st.cache_data
def generate_sample_data():
    """Generate a sample dataset with 50 rows and 4 meaningful features"""
    np.random.seed(42)
    
    # Generate dates for 50 consecutive days
    start_date = datetime(2024, 1, 1)
    dates = [start_date + timedelta(days=i) for i in range(50)]
    
    # Generate store data
    stores = np.random.choice(['Store_A', 'Store_B', 'Store_C', 'Store_D', 'Store_E'], 50)
    
    # Generate sales data (correlated with store type)
    store_multipliers = {'Store_A': 1.2, 'Store_B': 1.0, 'Store_C': 0.8, 'Store_D': 1.5, 'Store_E': 0.9}
    base_sales = np.random.normal(3000, 500, 50)
    sales = [max(1000, base_sales[i] * store_multipliers[stores[i]]) for i in range(50)]
    
    # Generate customer data (correlated with sales)
    customers = [max(50, int(sale/25 + np.random.normal(0, 10))) for sale in sales]
    
    # Create DataFrame
    data = {
        'Date': dates,
        'Store': stores,
        'Sales': [round(s, 2) for s in sales],
        'Customers': customers
    }
    
    return pd.DataFrame(data)

# Tab 0 Content Function
def show_download_content(df):
    """Content for the download and follow-along tab"""
    st.markdown('<h2 class="tab-header">📥 Download & Follow Along</h2>', unsafe_allow_html=True)
    
    # Hero section
    st.markdown("""
    <div class="download-section">
        <h3>🎯 Hey! Download the CSV and Follow Along</h3>
        <p>Get hands-on experience by downloading our sample dataset and practicing alongside the tutorials! 
        This interactive approach will help you master pandas operations step by step.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Download section with columns
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("### 🚀 What You'll Get:")
        st.write("✅ **50 rows** of realistic retail sales data")
        st.write("✅ **4 columns**: Date, Store, Sales, and Customers")
        st.write("✅ **Real-world scenarios** to practice with")
        st.write("✅ **Perfect for learning** pandas operations")
        
        st.markdown("### 💡 How to Use:")
        st.write("1. Download the CSV file below")
        st.write("2. Open it in your favorite editor (Excel, VS Code, etc.)")
        st.write("3. Follow along with each tutorial tab")
        st.write("4. Practice the code examples yourself!")
    
    with col2:
        st.markdown("### 📁 Download Dataset")
        
        # Convert DataFrame to CSV for download
        csv_data = df.to_csv(index=False)
        
        # Create download button
        st.download_button(
            label="⬇️ Download CSV Dataset",
            data=csv_data,
            file_name="pandas_learning_dataset.csv",
            mime="text/csv",
            help="Click to download the dataset used in this tutorial",
            use_container_width=True
        )
        
        st.info("💾 File size: ~2KB\n📊 Format: CSV")
    
    # Dataset preview
    st.markdown("### 👀 Dataset Preview")
    st.write("Here's a sneak peek at what you'll be working with:")
    
    # Show dataset info
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Rows", len(df))
    with col2:
        st.metric("Total Columns", len(df.columns))
    with col3:
        st.metric("Stores", df['Store'].nunique())
    with col4:
        st.metric("Date Range", "50 days")
    
    # Interactive preview
    st.dataframe(
        df.head(10), 
        use_container_width=True,
        hide_index=True
    )
    
    # Quick stats
    with st.expander("📈 Quick Statistics"):
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Sales Statistics:**")
            st.write(f"• Average: ${df['Sales'].mean():.2f}")
            st.write(f"• Maximum: ${df['Sales'].max():.2f}")
            st.write(f"• Minimum: ${df['Sales'].min():.2f}")
        
        with col2:
            st.write("**Customer Statistics:**")
            st.write(f"• Average: {df['Customers'].mean():.0f}")
            st.write(f"• Maximum: {df['Customers'].max()}")
            st.write(f"• Minimum: {df['Customers'].min()}")
    
    # Next steps
    st.markdown("### 🎯 Ready to Start?")
    st.success("Once you've downloaded the dataset, head over to the **🚀 Intro to Data Manipulation** tab to begin your pandas journey!")

# Main app
def main():    
    # Generate and cache the dataset
    df = generate_sample_data()
    
    # Store dataset in session state for access across tabs
    if 'df' not in st.session_state:
        st.session_state.df = df
    
    # Sidebar with dataset info
    with st.sidebar:
        st.markdown("## 📊 Dataset Overview")
        st.write(f"**Rows:** {len(df)}")
        st.write(f"**Columns:** {len(df.columns)}")
        st.write("**Features:**")
        for col in df.columns:
            st.write(f"- {col}")
        
        st.markdown("## 📖 Learning Objectives")
        st.write("""
        - Master DataFrame operations
        - Learn data aggregation techniques
        - Understand indexing and slicing
        - Create compelling visualizations
        - Handle missing data effectively
        """)
    
    # Create tabs with Tab 0 added
    tab0, tab1, tab2, tab3, tab4 = st.tabs([
        "📥 Download & Follow Along",
        "🚀 Intro to Data Manipulation",
        "📊 Aggregating DataFrames", 
        "🔍 Slicing and Indexing",
        "📈 Creating and Visualizing"
    ])
    
    with tab0:
        show_download_content(df)
    
    with tab1:
        tab1_intro.show_content(df)
    
    with tab2:
        tab2_aggregating.show_content(df)
    
    with tab3:
        tab3_slicing.show_content(df)
    
    with tab4:
        tab4_creating_viz.show_content(df)

if __name__ == "__main__":
    main()