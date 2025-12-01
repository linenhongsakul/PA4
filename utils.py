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
        return call_gemini_api(api_key, prompt)

if __name__ == '__main__':
    api_key = "AIzaSyD_9P-QWjjJKd23chwPSxpbmC72Dhiyx5Q"
    print(generate_question(api_key=api_key,
                            passage=""""Marie Curie is probably the most famous woman scientist who has ever lived. Born
Maria Sklodowska in Poland in 1867, she is famous for her work on radioactivity, and
was twice a winner of the Nobel Prize. With her husband, Pierre Curie, and Henri
Becquerel, she was awarded the 1903 Nobel Prize for Physics, and was then sole winner
of the 1911 Nobel Prize for Chemistry. She was the first woman to win a Nobel Prize.
                            """,
                            type="true_false_not_given"))
