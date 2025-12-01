import streamlit as st
import utils import generate_questions

with st.sidebar:
    api_key = st.text_input(label="API key",
                            type="password",
                            placeholder="Paste API key here...")

st.title("Generate IELTS-Style Questions")
st.text("Paste your reading passage into the text field below and click the button to generate practice qualifications and answers")

st.subheader("Reading Passage")
st.text_area(label="**Reading Passage**",
             placeholder="Paste the full text of your reading passage here...",
             height=400)

st.button(label=" ✨ Generate Questions",
          type="primary")

st.divider()

st.header("Generated Questions & Answers")

#True /False/ Not Given
with st.container(border=True):
    st.subheader("True/ False/ Not given")
    st.markdown(f"**1. This is the first question.**")
    st.markdown(f"Answer: FALSE")
    st.markdown(f"this is the description.")

#Multiple choices 
with st.container(border=True):
    st.subheader("Multiple Choices")
    st.markdown(f"**2. This is the second question.**")
    st.markdown(f"A)")
    st.markdown(f"B)")
    st.markdown(f"C)")
    st.markdown(f"D)")
    st.markdown(f"Answer is B")

#Short questions

