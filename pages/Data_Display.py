import streamlit as st
import pandas as pd

st.header("Data Display Demo")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Score": [85.5, 90.0, 88.5, 92.0]
})

# Display DataFrame
st.subheader("DataFrame Display")
st.dataframe(df, use_container_width=True)

# Static table
st.subheader("Static Table")
st.table(df)

# Metrics
st.subheader("Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Average Age", f"{df['Age'].mean():.1f}", "years")
col2.metric("Max Score", f"{df['Score'].max()}", "+2.0")
col3.metric("Min Score", f"{df['Score'].min()}", "-1.5")

# JSON display
st.subheader("JSON Display")
st.json({"key": "value", "numbers": [1, 2, 3], "nested": {"a": 1, "b": 2}})