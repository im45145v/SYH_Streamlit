import streamlit as st
import os
import importlib.util

# Set up the sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home", "About", "Thanos Snap", "Trivia Quiz", "Hero or Villain Detector"]
selection = st.sidebar.radio("Go to", pages)

# Load the pages from the `pages/` directory
def load_page(page_name):
    page_path = os.path.join("pages", f"{page_name.lower()}.py")
    spec = importlib.util.spec_from_file_location(page_name, page_path)
    page = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(page)
    return page

if selection == "Home":
    home = load_page("home")
    home.main()
elif selection == "About":
    about = load_page("about")
    about.main()
elif selection == "Thanos Snap":
    thanos_snap = load_page("thanos_snap")
    thanos_snap.main()
elif selection == "Trivia Quiz":
    trivia_quiz = load_page("trivia_quiz")
    trivia_quiz.main()
elif selection == "Hero or Villain Detector":
    hero_villain_detector = load_page("hero_villain_detector")
    hero_villain_detector.main()
