import streamlit as st
import pandas as pd

# Task 1: Build the App
st.title("Sales Summary App")
st.subheader("A simple app to view sales data filtered by category.")

# Hardcoded Dataset
data = {
    'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Speakers'],
    'Category': ['Electronics', 'Accessories', 'Accessories', 'Electronics','Accessories'],
    'Sales': [1200, 25, 75, 300, 60]
}
df = pd.DataFrame(data)

# Add a selectbox for category filtering in the sidebar
all_categories = ['All'] + list(df['Category'].unique())
selected_category = st.sidebar.selectbox("Select a Category to filter", all_categories)

# Filter the DataFrame based on the selected category
if selected_category == 'All':
    filtered_df = df
else:
    filtered_df = df[df['Category'] == selected_category]

# Display the filtered DataFrame
st.dataframe(filtered_df)

# Display a line chart of Sales values
st.line_chart(filtered_df['Sales'])