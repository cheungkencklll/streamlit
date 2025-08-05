import streamlit as st
import time

st.header("Interactive Widgets Demo")

# Text input and output
name = st.text_input("Enter your name", "Type here...")
st.write(f"Hello, {name}!")

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=120, value=25)
st.write(f"You are {age} years old.")

# Selectbox and multiselect
favorite_color = st.selectbox("Choose your favorite color", ["Red", "Blue", "Green"])
hobbies = st.multiselect("Select your hobbies", ["Reading", "Gaming", "Sports", "Cooking"])
st.write(f"Your favorite color is {favorite_color}")
st.write("Your hobbies:", ", ".join(hobbies) if hobbies else "None selected")

# Slider
st.subheader("Slider")
temperature = st.slider("Select temperature (°C)", -10, 40, 20)
st.write(f"Selected temperature: {temperature}°C")

# Buttons
st.subheader("Button")
if st.button("Click me!"):
    st.success("Button clicked!")

# Checkbox
st.subheader("Checkbox")
agree = st.checkbox("I agree to the terms")
st.write("Agreement status:", agree)

# Radio buttons
st.subheader("Radio Button")
mood = st.radio("What's your mood?", ["Happy", "Neutral", "Sad"])
st.write(f"You're feeling: {mood}")

# Date and time input
st.subheader("Date & Time")
date = st.date_input("Pick a date")
time_input = st.time_input("Pick a time")
st.write(f"Selected date: {date}, time: {time_input}")

# Status messages
st.subheader("Status Messages")
with st.spinner("Loading..."):
    time.sleep(1)
st.success("Done!")
st.error("This is an error message")
st.warning("This is a warning message")
st.info("This is an info message")

# Progress Demo
st.subheader("Progress")
progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i + 1)

