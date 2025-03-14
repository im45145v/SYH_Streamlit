import streamlit as st
import random

def main():
    st.title("Thanos Snap Simulator")
    st.write("Click the Snap! button to see if you survived or got dusted…")

    thanos_ascii_art = '''
⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀
⠀⠀⣠⣿⣿⣿⡿⠻⣿⣿⣿⣿⣿⣿⠟⢿⣿⣿⣿⣆⠀⠀
⠀⢠⣿⣿⣯⣉⣿⣄⣹⣿⣿⣿⣿⣏⣠⣟⡉⣽⣿⣿⡄⠀
⠀⢸⣿⣿⠟⠛⠉⠉⠛⠻⣿⣿⠟⠛⠉⠙⠛⢿⣿⣿⡇⠀
⣠⣾⣿⣿⣶⣾⡀⠀⣴⣦⣾⣷⣴⣆⠀⣀⣷⣾⣿⣿⣷⡄
⣿⣿⣿⣿⠟⢿⡿⠻⣿⣿⣿⣿⣿⣿⠿⢿⡿⠻⣿⣿⣿⡇
⢻⣿⣿⣿⣧⠈⢿⡀⠹⣄⣈⣁⣰⠏⢠⡿⠀⣼⣿⣿⣿⡇
⠀⣿⣿⣿⣿⣧⠀⣿⣀⣹⣿⣿⣇⣠⣿⠀⣼⣿⣿⣿⣿⠀
⠀⣿⣿⣿⣿⣿⡿⠿⠛⠛⠛⠛⠛⠛⠻⢿⣿⣿⣿⣿⣿⠀
⠀⢿⣿⣿⣿⣿⣀⣀⣤⣴⣶⣶⣦⣤⣀⣀⣿⣿⣿⣿⡟⠀
⠀⠘⣿⣿⣿⡟⢻⣿⠉⣿⡇⢸⣿⠉⣿⡟⢻⣿⣿⣿⠁⠀
⠀⠀⠸⣿⣿⡇⢸⣿⠀⣿⡇⢸⣿⠀⣿⡇⢸⣿⣿⠇⠀⠀
⠀⠀⠀⠹⣿⡇⢸⣿⠀⣿⡇⢸⣿⠀⣿⡇⢸⣿⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠁⠈⠉⠀⠉⠁⠈⠉⠀⠉⠁⠈⠀⠀⠀⠀⠀'''

    st.write(thanos_ascii_art)

    entropy = st.slider("Adjust Entropy", 0, 100, 50)

    if st.button("Snap!"):
        if random.randint(0, 100) < entropy:
            result = "You got dusted…"
        else:
            result = "You survived!"
        st.write(result)
        st.image("https://art.pixilart.com/d9aeb66792ae67c.gif")

if __name__ == "__main__":
    main()
