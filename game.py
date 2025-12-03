import streamlit as st
import random

# Set up the title and instructions
st.title("Number Guessing Game")
st.write("I am thinking of a number between 1 and 100.")
st.write("Try to guess it!")

# Generate a random number
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1, 100)
    st.session_state.attempts = 0

# User input for guess
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check the guess
if guess:
    st.session_state.attempts += 1
    if guess < st.session_state.number:
        st.write("Your guess is too low! Try again.")
    elif guess > st.session_state.number:
        st.write("Your guess is too high! Try again.")
    else:
        st.write(f"Congratulations! You've guessed the number in {st.session_state.attempts} attempts.")
        # Reset the game
        if st.button("Play Again"):
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0
