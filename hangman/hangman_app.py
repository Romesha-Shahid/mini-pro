import streamlit as st
import random

# Sample word list
WORDS = ["python", "streamlit", "hangman", "developer", "awesome", "project"]

# Initialize game state
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS).upper()
    st.session_state.guessed = []
    st.session_state.wrong_guesses = 0
    st.session_state.max_wrong = 6
    st.session_state.game_over = False

st.title("🔤 Hangman Game")
st.markdown("Guess the word by entering one letter at a time.")

# Show current progress
def get_display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

display_word = get_display_word(st.session_state.word, st.session_state.guessed)
st.markdown(f"### Word: `{display_word}`")

# Guess input
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter:", max_chars=1).upper()

    if st.button("Guess"):
        if guess in st.session_state.guessed:
            st.warning("You already guessed that letter.")
        elif guess.isalpha() and len(guess) == 1:
            st.session_state.guessed.append(guess)

            if guess not in st.session_state.word:
                st.session_state.wrong_guesses += 1
                st.error(f"Wrong guess! You have {st.session_state.max_wrong - st.session_state.wrong_guesses} tries left.")
        else:
            st.warning("Please enter a valid single letter.")

    # Show hangman status
    st.markdown(f"**Wrong guesses:** {st.session_state.wrong_guesses} / {st.session_state.max_wrong}")

    # Check win
    if all(letter in st.session_state.guessed for letter in st.session_state.word):
        st.success(f"🎉 Congratulations! You guessed the word: {st.session_state.word}")
        st.session_state.game_over = True

    # Check lose
    elif st.session_state.wrong_guesses >= st.session_state.max_wrong:
        st.error(f"💀 Game Over! The word was: {st.session_state.word}")
        st.session_state.game_over = True
else:
    if st.button("Play Again"):
        st.session_state.word = random.choice(WORDS).upper()
        st.session_state.guessed = []
        st.session_state.wrong_guesses = 0
        st.session_state.game_over = False
