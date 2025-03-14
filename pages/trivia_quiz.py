import streamlit as st
import time

def display_trivia_quiz():
    st.title("Marvel Trivia Quiz")

    # Question 1: Radio button
    st.subheader("Question 1")
    question1 = "Who is the first Avenger?"
    options1 = ["Iron Man", "Captain America", "Thor", "Hulk"]
    answer1 = "Captain America"
    user_answer1 = st.radio(question1, options1)

    # Question 2: Drop down
    st.subheader("Question 2")
    question2 = "What is the real name of Black Panther?"
    options2 = ["T'Challa", "M'Baku", "N'Jadaka", "Zuri"]
    answer2 = "T'Challa"
    user_answer2 = st.selectbox(question2, options2)

    # Question 3: Text box
    st.subheader("Question 3")
    question3 = "What is the name of Thor's hammer?"
    answer3 = "Mjolnir"
    user_answer3 = st.text_input(question3)

    # Question 4: Multi-select
    st.subheader("Question 4")
    question4 = "Which of the following are Infinity Stones?"
    options4 = ["Time Stone", "Power Stone", "Reality Stone", "Soul Stone", "Mind Stone", "Space Stone", "Love Stone"]
    answer4 = ["Time Stone", "Power Stone", "Reality Stone", "Soul Stone", "Mind Stone", "Space Stone"]
    user_answer4 = st.multiselect(question4, options4)

    if st.button("Submit"):
        score = calculate_score(user_answer1, answer1, user_answer2, answer2, user_answer3, answer3, user_answer4, answer4)
        provide_feedback(score)

def calculate_score(user_answer1, answer1, user_answer2, answer2, user_answer3, answer3, user_answer4, answer4):
    score = 0
    if user_answer1 == answer1:
        score += 1
    if user_answer2 == answer2:
        score += 1
    if user_answer3.lower() == answer3.lower():
        score += 1
    if set(user_answer4) == set(answer4):
        score += 1

    # Animation
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)

    return score

def provide_feedback(score):
    st.subheader("Feedback")
    if score == 4:
        st.success(f"Congratulations! You scored {score}/4.")
    else:
        st.error(f"You scored {score}/4. Better luck next time!")

def main():
    display_trivia_quiz()

if __name__ == "__main__":
    main()
