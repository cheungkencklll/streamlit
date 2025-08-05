import streamlit as st

st.header("Layout Features Demo")

# Columns
with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Column 1")
        st.write("This is the first column")
        st.button("Button in Col1")

    with col2:
        st.subheader("Column 2")
        st.slider("Slider in Col2", 0, 100, 50)

    with col3:
        st.subheader("Column 3")
        st.selectbox("Select in Col3", ["Option 1", "Option 2", "Option 3"])

# Tabs
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Content in Tab 1")
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png")

with tab2:
    st.write("Content in Tab 2")
    st.checkbox("Checkbox in Tab 2")

# Expander
with st.expander("Click to expand"):
    st.write("This content is hidden until expanded")
    st.slider("Hidden slider", 0, 10, 5)