import streamlit as st
import random

# Title
st.title("🎯 Guess the Number (You vs Computer)")

st.markdown("Guess the number I'm thinking of between **1 and 100**.")

# Initialize the number once per session
if "target_number" not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

# User input
if not st.session_state.game_over:
    guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        target = st.session_state.target_number

        if guess < target:
            st.info("Too low! Try again.")
        elif guess > target:
            st.info("Too high! Try again.")
        else:
            st.success(f"🎉 Correct! The number was {target}.")
            st.balloons()
            st.write(f"You guessed it in **{st.session_state.attempts}** attempts.")
            st.session_state.game_over = True
else:
    if st.button("Play Again"):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
