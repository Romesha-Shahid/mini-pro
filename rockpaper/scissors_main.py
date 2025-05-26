import streamlit as st
import random

# Title
st.title("✊✋✌️ Rock, Paper, Scissors Game")

# Choices
choices = ["Rock", "Paper", "Scissors"]

# User selection
user_choice = st.selectbox("Choose your move:", choices)

# Play button
if st.button("Play"):
    computer_choice = random.choice(choices)

    st.write(f"🤖 Computer chose: **{computer_choice}**")
    st.write(f"🧍 You chose: **{user_choice}**")

    # Determine winner
    if user_choice == computer_choice:
        st.info("It's a tie!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        st.success("🎉 You win!")
    else:
        st.error("😞 You lose!")
