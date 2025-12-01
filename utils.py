import google.generativeai as genai
import json
from typing import Literal

def call_gemini_api(api_key: str,prompt:str):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash-lithe")
    data = model.generate_content (prompt,
                                   generative_config={
                                       "response_mime_type": "application/json"
                                   })
    data = json.loads(response.text)
                                    

def generate_question(api_key:str,
                      passage: str,
                      type: Literal["true_false_not_given",
                                    "multiple_choices",
                                    "short_answer"]):
    pass
