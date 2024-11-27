# Importing the Streamlit library
# Streamlit is a Python library that lets you create web apps quickly and easily
import streamlit as st  # st is the commonly used alias for Streamlit

# Setting the title of the app
# The title will appear at the top of your web app
st.title("Hello, World! 🌎")

# Adding a header to the app
# Headers are slightly smaller than the title and help structure the content
st.header("Welcome to Your First Streamlit App 🎉")

# Adding a text section
# This will explain what the app is doing, helpful for learning
st.write("""
This is your first Streamlit app. Below, we will print debug messages to understand
how everything works. Follow these steps:
1. Run this script using the Streamlit CLI.
2. Open the app in your browser.
3. Confirm the output matches the code.
""")

# Debugging section (on-screen and console debugging)
# Print statements are included for console-based debugging
print("Streamlit app is running!")  # This will print to your terminal

# Adding an interactive button
# This is to demonstrate interactivity in Streamlit
if st.button("Click Me!"):
    st.write("You clicked the button. 🎉 Well done!")
    print("Button was clicked.")  # Debug message

# Final note for learning
st.write("Feel free to modify this code and observe changes in real time!")

# Console debugging
print("App loaded successfully.")
