import streamlit as st
from utils import generate_question
import pandas as pd

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
    question_df = pd.DataFrame(columns=["id", "question_type", "question", "choices", "answer", "description"])
    question_id = 1

    st.header("Generated Questions & Answers")
    # True / False / Not Given
    with st.container(border=True):
        st.subheader("True / False / Not Given")
        for i in range(3):
            data = generate_question(api_key=api_key,
                                    passage=passage,
                                    type="true_false_not_given")
            
            st.markdown(f"**{question_id}. {data['question']}**")
            st.markdown(f"Answer: **{data['answer']}**")
            st.markdown(data["description"])

            question_df.loc[len(question_df)] = {
                "id": question_id,
                "question_type": "true_false_not_given",
                "question": data["question"],
                "choices": "TRUE / FALSE / NOT GIVEN",
                "answer": data['answer'],
                "description": data["description"]
            }

            question_id += 1
        
    # Multiple choice
    with st.container(border=True):
        st.subheader("Multiple Choice")
        for i in range(3):
            data = generate_question(api_key=api_key,
                                    passage=passage,
                                    type="multiple_choice")
            
            st.markdown(f"**{question_id}. {data['question']}**")
            for choice, choice_description in data['options'].items():
                if choice == data['answer']:
                    st.markdown(f"**{choice}. {choice_description}**")
                else:
                    st.markdown(f"{choice}. {choice_description}")
            st.markdown(f"Answer: **{data['answer']}**")
            st.markdown(data["description"])
            question_df.loc[len(question_df)] = {
                "id": question_id,
                "question_type": "multiple_choice",
                 "question": data["question"],
                "choices": data['options'],
                "answer": data['answer'],
                "description": data["description"]
            }
            
            question_id += 1        

    # Short Answer Questions
    with st.container(border=True):
        st.subheader("Short Answer Questions")
        for i in range(4):

            data = generate_question(api_key=api_key,
                                    passage=passage,
                                    type="short_answer")
            
            st.markdown(f"**{question_id}. {data['question']}**")
            st.markdown(f"Answer: **{data['answer']}**")
            st.markdown(data["description"])

            question_df.loc[len(question_df)] = {
                "id": question_id,
                "question_type": "short_answer",
                "question": data["question"],
                "choices": "",
                "answer": data['answer'],
                "description": data["description"]
            }

            question_id += 1

    @st.cache_data
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df(question_df)

    st.subheader("Question Dataframe")
    st.dataframe(data=question_df)
    st.download_button(
        label="Press to Download",
        data=csv,
        file_name="IELTS-style questions.csv",
        mime="text/csv",
        key='download-csv'
    )
