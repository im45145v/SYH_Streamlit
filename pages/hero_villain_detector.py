import streamlit as st
import random
from streamlit_webrtc import webrtc_streamer
import av

def detect_hero_or_villain():
    return random.choice(["🦸 You're a Hero!", "🦹 You're a Villain!"])

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")
    return av.VideoFrame.from_ndarray(img, format="bgr24")

def main():
    st.title("Hero or Villain Detector")
    st.write("Upload a photo or use the camera to find out if you're a hero or a villain!")

    uploaded_file = st.file_uploader("Choose a photo...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Photo", use_column_width=True)
        result = detect_hero_or_villain()
        st.write(result)

    # if st.button("Use Camera"):
    #     webrtc_streamer(key="example", video_frame_callback=video_frame_callback)
    #     result = detect_hero_or_villain()
    #     st.write(result)

if __name__ == "__main__":
    main()
