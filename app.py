# app.py

import streamlit as st

# Title of the app
st.title("📊 Simple Streamlit Demo")

# Header
st.header("User Input and Plotting")

# Text input
name = st.text_input("Enter your name:", "World")
st.write(f"Hello, {name}!")

# Slider input
slider_val = st.slider("Select a value", 0, 100, 25)
st.write(f"Slider value is: {slider_val}")


st.caption("Made with ❤️ using Streamlit")
