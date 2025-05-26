import streamlit as st
import random

# Set title
st.title("🎯 Guess the Number Game")

if "number_to_guess" not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0

# Input from user
guess = st.number_input("Enter your guess (1 to 100):", min_value=1, max_value=100, step=1)

# Guess button
if st.button("Submit Guess"):
    st.session_state.attempts += 1
    number = st.session_state.number_to_guess

    if guess < number:
        st.warning("Too low! Try again.")
    elif guess > number:
        st.warning("Too high! Try again.")
    else:
        st.success(f"🎉 Correct! You guessed it in {st.session_state.attempts} tries.")
        st.balloons()
        # Reset the game
        if st.button("Play Again"):
            st.session_state.number_to_guess = random.randint(1, 100)
            st.session_state.attempts = 0
