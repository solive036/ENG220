import streamlit as st

# Set the title of the app
st.title("Simple Message Display App")

# Create a text input box for the user to enter a message
user_message = st.text_input("Enter your message:")

# Display the message if there is any input
if user_message:
    st.write("You entered: ", user_message)

