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

    # # Add a new tab for the hero or villain detector functionality
    # tabs = st.tabs(["Home", "Hero or Villain Detector"])
    # with tabs[0]:
    #     st.write("This is the home tab.")
    # with tabs[1]:
    #     st.title("Hero or Villain Detector")
    #     st.write("Upload a photo or use the camera to find out if you're a hero or a villain!")

    #     uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])
    #     if uploaded_file is not None:
    #         st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)
    #         result = detect_hero_or_villain()
    #         st.write(result)

    #     if st.button("Use Camera"):
    #         webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
    #         result = detect_hero_or_villain()
    #         st.write(result)

if __name__ == "__main__":
    main()
