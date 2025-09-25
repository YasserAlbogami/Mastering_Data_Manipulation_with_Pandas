---
# 🐼 Pandas Learning Hub: Interactive Data Manipulation Tutorial

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://masteringdatamanipulationwithpandas-hdskjthujlbfjtt8faw4gn.streamlit.app/)
[![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pandas](https://img.shields.io/badge/pandas-v2.0+-green.svg)](https://pandas.pydata.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Master Data Manipulation with Pandas through Interactive Learning**

A comprehensive, interactive Streamlit application designed to teach data manipulation using Pandas through hands-on exercises, real-world examples, and immediate visual feedback.

---

## 🚀 Launch the App

<div align="center">

<a href="https://masteringdatamanipulationwithpandas-hdskjthujlbfjtt8faw4gn.streamlit.app/" target="_blank" style="text-decoration:none;">
    <img src="https://static.streamlit.io/badges/streamlit_badge_black_white.svg" alt="Open in Streamlit" height="35">
</a>

<br><br>

<a href="https://masteringdatamanipulationwithpandas-hdskjthujlbfjtt8faw4gn.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/Launch%20App-Streamlit-green?logo=streamlit&logoColor=white&labelColor=black&style=for-the-badge" alt="Launch App" style="margin-top: 12px; margin-bottom: 12px;"/>
</a>

</div>

You can **visit the live app here**:  
[https://masteringdatamanipulationwithpandas-hdskjthujlbfjtt8faw4gn.streamlit.app/](https://masteringdatamanipulationwithpandas-hdskjthujlbfjtt8faw4gn.streamlit.app/)

---

## 🌟 Features

### 📚 **4 Comprehensive Learning Modules**
- **Intro to Data Manipulation** - Foundation concepts and DataFrame basics
- **Aggregating DataFrames** - Statistical summaries and grouping operations  
- **Slicing and Indexing** - Advanced data selection and filtering techniques
- **Creating and Visualizing** - Data creation, visualization, and export methods

### 🎯 **Interactive Learning Experience**
- ✅ **50+ Code Examples** with live execution
- ✅ **Real Dataset** (50 rows, 4 features) for practical learning
- ✅ **Immediate Visual Output** for every code snippet
- ✅ **Progressive Difficulty** from beginner to advanced concepts
- ✅ **Professional Visualizations** using Matplotlib and Seaborn

### 🔧 **Technical Highlights**
- **Modular Architecture** with separate tab components
- **Responsive Design** with custom CSS styling
- **Memory Efficient** with Streamlit caching
- **Production Ready** with comprehensive error handling

---

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip package manager
```

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YasserAlbogami/data_persona.git
   cd data_persona
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run pandas_learning_app.py
   ```

4. **Open your browser** to `http://localhost:8501`

---

## 📁 Project Structure

```
data_persona/
├── 📄 pandas_learning_app.py          # Main Streamlit application
├── 📁 tabs/                           # Modular tab components
│   ├── __init__.py                    # Package initializer
│   ├── tab1_intro.py                  # Introduction to Data Manipulation
│   ├── tab2_aggregating.py            # Aggregating DataFrames
│   ├── tab3_slicing.py                # Slicing and Indexing
│   └── tab4_creating_viz.py           # Creating and Visualizing
├── 📄 requirements.txt                # Python dependencies
└── 📄 README.md                       # Project documentation
```

---

## 📊 Dataset Overview

The application uses a **carefully crafted 50-row dataset** with realistic business metrics:

| Feature | Description | Type | Range/Values |
|---------|-------------|------|--------------|
| **Date** | Sales date (50 consecutive days) | DateTime | 2024-01-01 to 2024-02-19 |
| **Store** | Store identifier | Categorical | Store_A, Store_B, Store_C, Store_D, Store_E |
| **Sales** | Daily sales revenue | Numeric | $1,000 - $5,000 |
| **Customers** | Daily customer count | Integer | 50 - 200 customers |

### Sample Data Preview
```python
        Date     Store    Sales  Customers
0 2024-01-01   Store_A  3425.67        142
1 2024-01-02   Store_B  2876.43        118
2 2024-01-03   Store_E  2654.89         98
```

---

## 🎓 Learning Modules

### 📖 **Module 1: Introduction to Data Manipulation**
Master the fundamentals of DataFrame operations:
- DataFrame structure and components
- Data inspection techniques
- Sorting and basic filtering
- Column creation and manipulation

**Key Skills:** `df.head()`, `df.info()`, `df.sort_values()`, `df[]` selection

### 📊 **Module 2: Aggregating DataFrames** 
Learn statistical analysis and data summarization:
- Descriptive statistics and summaries
- GroupBy operations and aggregations
- Pivot tables and cross-tabulations
- Time-based aggregations

**Key Skills:** `df.groupby()`, `df.agg()`, `df.pivot_table()`, `df.describe()`

### 🔍 **Module 3: Slicing and Indexing**
Master advanced data selection techniques:
- Index manipulation and multi-level indexing
- Label-based selection with `.loc[]`
- Position-based selection with `.iloc[]`
- Boolean indexing and query operations

**Key Skills:** `df.set_index()`, `df.loc[]`, `df.iloc[]`, `df.query()`

### 📈 **Module 4: Creating and Visualizing**
Learn data creation, visualization, and export:
- Data visualization with Matplotlib/Seaborn
- Missing value detection and handling
- DataFrame creation from various sources
- CSV import/export operations

**Key Skills:** `plt.plot()`, `sns.boxplot()`, `df.fillna()`, `pd.read_csv()`

---

## 🛠️ Technical Implementation

### **Core Technologies**
- **Frontend:** Streamlit 1.28+ for interactive web interface
- **Data Processing:** Pandas 2.0+ for data manipulation
- **Visualization:** Matplotlib 3.7+ and Seaborn 0.12+ for charts
- **Scientific Computing:** NumPy 1.24+ for numerical operations

### **Architecture Patterns**
- **Modular Design:** Separate files for each learning module
- **Session State Management:** Efficient data sharing across tabs
- **Caching Strategy:** `@st.cache_data` for performance optimization
- **Responsive Layout:** Dynamic column layouts and mobile compatibility

### **Code Quality**
- **PEP 8 Compliance:** Clean, readable code structure
- **Type Hints:** Enhanced code documentation
- **Error Handling:** Robust exception management
- **Documentation:** Comprehensive inline comments

---

## 🎨 User Interface

### **Design Philosophy**
- **Clean Minimal Interface** focusing on content
- **Syntax Highlighted Code** blocks for clarity
- **Immediate Visual Feedback** for every operation
- **Professional Color Scheme** for better readability

### **Interactive Elements**
- **Tabbed Navigation** for organized learning progression
- **Expandable Sections** for detailed explanations
- **Live Code Execution** with real-time outputs
- **Dynamic Visualizations** responding to data changes

---

## 📚 Educational Approach

### **Learning Methodology**
1. **Concept Introduction** - Clear theoretical explanation
2. **Code Example** - Practical implementation
3. **Live Execution** - Immediate visual results
4. **Progressive Complexity** - Building upon previous concepts

### **Target Audience**
- **Data Science Students** learning Pandas fundamentals
- **Business Analysts** transitioning to Python
- **Software Developers** expanding data skills
- **Researchers** needing data manipulation techniques

---

## 🔧 Customization Guide

### **Adding New Examples**
```python
# In any tab file (e.g., tab1_intro.py)
def show_content(df):
    st.markdown("## Your New Section")
    st.markdown("Description of the concept...")
    
    code = '''
    # Your example code here
    result = df.your_operation()
    '''
    st.code(code, language="python")
    
    # Execute and display results
    result = df.your_operation()
    st.dataframe(result)
```

### **Modifying the Dataset**
```python
# In pandas_learning_app.py
@st.cache_data
def generate_sample_data():
    # Modify this function to change the dataset
    # Add new columns, change data ranges, etc.
    pass
```

### **Styling Customization**
```python
# Modify the CSS in pandas_learning_app.py
st.markdown("""
<style>
    .your-custom-class {
        /* Your custom styling */
    }
</style>
""", unsafe_allow_html=True)
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### **Ways to Contribute**
- 🐛 **Bug Reports** - Find and report issues
- 💡 **Feature Requests** - Suggest new learning modules
- 📝 **Documentation** - Improve tutorials and examples
- 🎨 **UI/UX** - Enhance user interface design
- 📊 **Datasets** - Contribute interesting example datasets

### **Development Setup**
```bash
# Fork the repository
git clone https://github.com/YourUsername/data_persona.git
cd data_persona

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
pip install black flake8 pytest  # Development tools

# Make your changes and test
streamlit run pandas_learning_app.py

# Submit pull request
```


## 🔗 Related Projects

### **Educational Resources**
- [Official Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [10 Minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html)

### **Similar Projects**
- [Streamlit Gallery](https://streamlit.io/gallery) - More Streamlit examples
- [Plotly Dash](https://dash.plotly.com/) - Alternative dashboard framework
- [Jupyter Notebooks](https://jupyter.org/) - Interactive computing environment

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Yasser Albogami

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

**Yasser Albogami**
- 🐙 GitHub: [@YasserAlbogami](https://github.com/YasserAlbogami)
- 💼 LinkedIn: [Connect with me](https://linkedin.com/in/yasseralbogami)
- 📧 Email: yasserayalbogami@gmail.com

---

## 🙏 Acknowledgments

- **Pandas Development Team** for the amazing library
- **Streamlit Team** for the excellent framework
- **Python Community** for continuous inspiration
- **Data Science Community** for feedback and suggestions

---

## 📊 Project Stats

![GitHub stars](https://img.shields.io/github/stars/YasserAlbogami/data_persona?style=social)
![GitHub forks](https://img.shields.io/github/forks/YasserAlbogami/data_persona?style=social)
![GitHub issues](https://img.shields.io/github/issues/YasserAlbogami/data_persona)
![GitHub pull requests](https://img.shields.io/github/issues-pr/YasserAlbogami/data_persona)

**⭐ Star this repository if you find it helpful!**

---

<div align="center">

### 🚀 Ready to Master Pandas?

[**Launch App**](https://masteringdatamanipulationwithpandas-hdskjthujlbfjtt8faw4gn.streamlit.app/) | [**View Source**](https://github.com/YasserAlbogami/data_persona) | [**Report Bug**](https://github.com/YasserAlbogami/data_persona/issues)

**Happy Learning! 🐼📊**

</div>
