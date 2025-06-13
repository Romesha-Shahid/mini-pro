import streamlit as st   
import random  
import string  


def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters  

    if use_digits:
        characters += string.digits

    if use_special:
        characters += (
            string.punctuation
        )  

    
    return "".join(random.choice(characters) for _ in range(length))


# Streamlit UI setup
st.title("Simple Password Generator")  

length = st.slider("Select password length:", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include numbers")  # Checkbox for numbers (0-9)
use_special = st.checkbox(
    "Include special characters"
)  # Checkbox for special characters (!@#$%^&*)

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(
        length, use_digits, use_special
    )  
    st.write(f"Generated Password: `{password}`")  # Display the generated password