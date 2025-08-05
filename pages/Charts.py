import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

st.header("Charts Demo")

# Sample data for charts
chart_data = pd.DataFrame(
    np.random.randn(100, 3),
    columns=['A', 'B', 'C']
)

# Line chart
st.subheader("Line Chart")
st.line_chart(chart_data)

# Area chart
st.subheader("Area Chart")
st.area_chart(chart_data)

# Bar chart
st.subheader("Bar Chart")
st.bar_chart(chart_data)

# Altair chart
st.subheader("Altair Chart")
altair_chart = alt.Chart(chart_data).mark_circle().encode(
    x='A', y='B', size='C', color='C'
)
st.altair_chart(altair_chart, use_container_width=True)

# Plotly scatter chart
st.subheader("Plotly Scatter Chart")
# Transform 'C' to ensure non-negative values for size
chart_data['C_scaled'] = (chart_data['C'] - chart_data['C'].min()) + 1  # Shift to positive and add 1 to avoid zero
chart_data['C_scaled'] = chart_data['C_scaled'] * 10  # Scale for better visibility
fig_scatter = px.scatter(chart_data, x='A', y='B', size='C_scaled', color='C')
st.plotly_chart(fig_scatter, use_container_width=True)

# Plotly pie chart
st.subheader("Plotly Pie Chart")
# Sample data for pie chart
pie_data = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [30, 20, 25, 25]
})
fig_pie = px.pie(pie_data, names="Category", values="Values", title="Sample Category Distribution")
st.plotly_chart(fig_pie, use_container_width=True)