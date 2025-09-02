# app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Checkbox
if st.checkbox("Show random data plot"):
    # Generate random data
    data = pd.DataFrame({
        'x': np.linspace(0, 10, 100),
        'y': np.sin(np.linspace(0, 10, 100) + slider_val / 10)
    })

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(data['x'], data['y'])
    ax.set_title("📈 Sine Wave with Offset")
    st.pyplot(fig)

# Button
if st.button("Click Me"):
    st.success("🎉 You clicked the button!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")
