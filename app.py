import streamlit as st
from utils import generate_question

with st.sidebar:
    api_key = st.text_input(label="API key",
                            type="password",
                            placeholder="Paste API key here...")

st.title("Generate IELTS-Style Questions")
st.text("Paste your reading passage into the text field below and click the button to generate practice questions and answers.")

passage = st.text_area(label="**Reading Passage**",
             placeholder="Paste the full text of your reading passage here...",
             height=400)

submit_button = st.button(label="✨ Generate Questions",
          type="primary")

st.divider()

if submit_button:
    st.header("Generated Questions & Answers")
    # True / False / Not Given
    with st.container(border=True):
        st.subheader("True / False / Not Given")
        data = generate_question(api_key=api_key,
                                passage=passage,
                                type="true_false_not_given")
        
        st.markdown(f"**1. {data['question']}**")
        st.markdown(f"Answer: {data['answer']}")
        st.markdown(data["description"])
        
    # Multiple choice
    with st.container(border=True):
        st.subheader("Multiple Choice")
        data = generate_question(api_key=api_key,
                                passage=passage,
                                type="multiple_choice")
        
        st.markdown(f"**2. {data['question']}**")
        st.markdown(f"Answer: {data['answer']}")
        st.markdown(data["description"])
        

    # Short Answer Questions
    with st.container(border=True):
        st.subheader("Short Answer Questions")
        data = generate_question(api_key=api_key,
                                passage=passage,
                                type="short_answer")
        
        st.markdown(f"**3. {data['question']}**")
        st.markdown(f"Answer: {data['answer']}")
        st.markdown(data["description"])
        


