import streamlit as st
import os
import importlib.util

# Set up the sidebar for navigation
st.sidebar.title("Navigation")
pages = ["Home", "About"]
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
