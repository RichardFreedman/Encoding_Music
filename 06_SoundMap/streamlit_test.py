import streamlit as st
import pandas as pd
import numpy as np

# Set up the page
st.title("Simple Scatter Plot Demo")
st.write("This app demonstrates a checkbox controlling a scatter plot display.")

# Create a checkbox in the sidebar
show_plot = st.sidebar.checkbox("Show Scatter Plot")

# Generate some simple sample data
np.random.seed(42)  # For reproducible results
n_points = 50
data = pd.DataFrame({
    'x': np.random.randn(n_points),
    'y': np.random.randn(n_points)
})

# Conditionally show the scatter plot based on checkbox state
if show_plot:
    st.subheader("Sample Scatter Plot")
    st.write("Here's your scatter plot with random data points:")
    
    # Display the scatter plot
    st.scatter_chart(
        data,
        x='x',
        y='y',
        width="stretch",
        height=400
    )
    
    # Optional: Show the data table as well
    with st.expander("View Raw Data"):
        st.dataframe(data)
else:
    st.write("👈 Check the box in the sidebar to display the scatter plot!")