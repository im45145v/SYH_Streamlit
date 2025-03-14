import streamlit as st
import random

def generate_superhero_name(real_name):
    prefixes = ["Captain", "Iron", "Spider", "Black", "Doctor", "Scarlet", "Silver", "Star", "Storm", "Thunder"]
    suffixes = ["Man", "Woman", "Hero", "Warrior", "Knight", "Guardian", "Avenger", "Crusader", "Champion", "Defender"]
    prefix = random.choice(prefixes)
    suffix = random.choice(suffixes)
    return f"{prefix} {suffix}"

def main():
    st.title("Welcome to the Marvel Streamlit App")
    st.write("This is the home page of the Marvel Streamlit App. Use the sidebar to navigate to different pages.")
    
    real_name = st.text_input("Enter your real name:")
    
    if st.button("Generate Superhero Name"):
        superhero_name = generate_superhero_name(real_name)
        st.write(f"Your Marvel-style superhero name is: {superhero_name}")
        st.balloons()  # Special effect: Balloons
    
    if st.button("Show Snow"):
        st.snow()  # Special effect: Snow
    
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)  # Special effect: Progress bar

if __name__ == "__main__":
    main()
