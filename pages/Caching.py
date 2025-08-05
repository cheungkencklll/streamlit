import streamlit as st
import time

st.header("Caching Demo")

# Caching example
@st.cache_data
def expensive_computation(x):
    time.sleep(2)
    return x * x

st.subheader("Caching Example")
number = st.slider("Select a number for caching demo", 1, 10, 5)
result = expensive_computation(number)
st.write(f"Cached result: {number} * {number} = {result}")