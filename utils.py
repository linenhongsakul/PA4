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
    
    elif type == "multiple_choice":
        prompt = """Generate an IELTS-style multiple choice Given question, based on the passage below.
        
        return the output in **strict JSON** format with the following structure.
        **Expected Output Schema**
        | Column | Type | Description |
        |---------|------|--------------|
        | question | str | IELTS-style question based on the passage |
        | answer | str | A / B / C / D |
        | description | str | Description of answer |
      
        
        Example:
        {
        "question": "In which year was Marie Curie born?",
        "options": {
            "A": "1867",
            "B": "1873",
            "C": "1881",
            "D": "1890"
        },
        "answer": "A",
        "description": "Marie Curie was born in Poland in 1867, as stated in the passage."
        },

        Passage:
        {passage}
        """
        return call_gemini_api(api_key, prompt)
    
    elif type == "short_answer":
        prompt = """Generate an IELTS-style question for short-answer based on the passage below.

        return the output in **strict JSON** format with the following structure.
        **Expected Output Schema**
        | Column | Type | Description |
        |---------|------|--------------|
        | question | str | IELTS-style question based on the passage |
        | answer | str | short answer |
        | description | str | Description of answer |

        Example:
         },
        "question": "Who were Marie Curie’s research partners when she won the 1903 Nobel Prize for Physics?",
        "answer": "Pierre Curie and Henri Becquerel",
        "description": "Marie Curie shared the 1903 Nobel Prize for Physics with her husband Pierre Curie and Henri Becquerel for their work on radioactivity."
        }

        Passage:
        {passage}
        """

    else:
        raise ValueError("Error")
        
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
