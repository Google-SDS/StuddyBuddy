import streamlit as st
import google.generativeai as genai

st.markdown('<style> p {text-align: center;} </style>', unsafe_allow_html=True)
genai.configure(api_key = 'AIzaSyAbl5wLTQ8JVD70xj2-6ZzVlboXwzbKt0A')

# GenAI model insertion into code.
def generate_text(prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

st.title("Proactivate")

st.subheader("Study doesn't have to be boring.")

st.title("About")

st.text(
    """
    Proactivate is a web/app designed to make studying easier and fun. We believe that 
    learning should be an active process, and our goal is to help you achieve you 
    academic success in a way that keeps you motivated.

    * Interactive Study Tools (Flashcards, Quizzes)
    * Personalized Study Plans
    * Gamification elements (like points, badges)
    """
)

st.title("How to use it")

st.text(
    """
    Step 1: Upload a file (it can be a PDF, or a text file) with the information you want to study.
    Step 2: Select the type of study tool you want to use.
    Step 3: Start studying!
    """
)

file = st.file_uploader("Upload a file")

if file is not None:
    st.write("You uploaded:", file.name)

    st.text("Select the type of study tool you want to use.")
    tool = st.radio(
        "",
        ("Flashcards", "Quizzes"),
    )

    ai_response = generate_text(tool)
    st.markdown(f"{ai_response}")
