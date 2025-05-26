# Make it funny story 
import streamlit as st

st.title("🌟 Mad Libs Generator with Streamlit")

st.header("Fill in the blanks 👇")

# Input fields
name = st.text_input("Enter a name:")
place = st.text_input("Enter a place:")
adjective = st.text_input("Enter an adjective:")
noun = st.text_input("Enter a noun:")
verb = st.text_input("Enter a verb ending with -ing:")
animal = st.text_input("Enter an animal:")

# Generate story
if st.button("Generate Story"):
    if name and place and adjective and noun and verb and animal:
        story = (
            f"One day, {name} was walking through the {place} when they saw a very {adjective} {animal}. "
            f"It was holding a {noun} and {verb} happily. {name} couldn't believe their eyes!"
        )
        st.success("Here's your story:")
        st.write(story)
    else:
        st.warning("Please fill in all the blanks!")
