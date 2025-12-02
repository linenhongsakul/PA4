import json
import google.generativeai as genai
from typing import Literal

def call_gemini_api(api_key: str, prompt: str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash-lite")
    response = model.generate_content(prompt,
                                      generation_config={
                                          "response_mime_type": "application/json"
                                      })

    data = json.loads(response.text)
    return data

def generate_question(api_key: str, 
                      passage: str, 
                      type: Literal["true_false_not_given",
                                    "multiple_choice",
                                    "short_answer"]):
    
    if type == "true_false_not_given":
        prompt = f"""Generate an IELTS-style True/False/Not Given question, based on the passage below.

        return the output in **strict JSON** format with the following structure.
        **Expected Output Schema**
        | Column | Type | Description |
        |---------|------|--------------|
        | question | str | IELTS-style question based on the passage |
        | answer | str | TRUE / FALSE / NOT GIVEN |
        | description | str | Description of answer |

        Example:
        {{
            "question": "Dinosaurs are the biggest animals to ever live on Earth.",
            "answer": FALSE,
            "description": Although dinosaurs were among the largest land animals to ever live on Earth, they were not the biggest animals. The blue whale, which is alive today, is actually larger than any known dinosaur.,
        }}

        Passage:
        {passage}
        """
    
    elif type == "multiple_choice":
        prompt = f"""Generate an IELTS-style multiple choice Given question, based on the passage below.
        
        return the output in **strict JSON** format with the following structure.
        **Expected Output Schema**
        | Column | Type | Description |
        |---------|------|--------------|
        | question | str | IELTS-style question based on the passage |
        | options | dict | 4 options for the question |
        | answer | str | A / B / C / D |
        | description | str | Description of answer |
      
        
        Example:
        {{
            "question": "What does a white belt usually represent in martial arts?",
            "options": {{
                "A": "Beginner level",
                "B": "Expert level",
                "C": "Instructor",
                "D": "Intermediate level"
            }},
            "answer": "A",
            "description": "White belts signify a beginner level, representing a clean slate and the start of training.",
        }}

        Passage:
        {passage}
        """
    
    elif type == "short_answer":
        prompt = f"""Generate an IELTS-style question for short-answer based on the passage below.

        return the output in **strict JSON** format with the following structure.
        **Expected Output Schema**
        | Column | Type | Description |
        |---------|------|--------------|
        | question | str | IELTS-style question based on the passage |
        | answer | str | short answer |
        | description | str | Description of answer |

        Example:
        {{
            "question": "What gas do plants absorb from the atmosphere during photosynthesis?",
            "answer": "Carbon dioxide",
            "description": "During photosynthesis, plants absorb carbon dioxide (CO2) and use sunlight to produce oxygen and glucose."
        }}

        Passage:
        {passage}
        """

    else:
        raise ValueError("Error")
        
    return call_gemini_api(api_key, prompt)