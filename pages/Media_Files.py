import streamlit as st
import pandas as pd

st.header("Media & Files Demo")

# Image display
st.subheader("Image Display")
st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", 
         caption="Streamlit Logo")

# Audio
st.subheader("Audio")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# Video
st.subheader("Video")
st.video("https://www.youtube.com/watch?v=1a_1M-3gqTI")

# File uploader
st.subheader("File Uploader")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write(f"Uploaded file: {uploaded_file.name}")
    if uploaded_file.type.startswith('text'):
        st.text(uploaded_file.read().decode('utf-8'))

# Download button
st.subheader("Download Button")
sample_csv = pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]}).to_csv()
st.download_button(
    label="Download sample CSV",
    data=sample_csv,
    file_name="sample_data.csv",
    mime="text/csv"
)