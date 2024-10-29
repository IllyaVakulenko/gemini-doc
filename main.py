import google.generativeai as genai
import os
from dotenv import load_dotenv
from modules.functions import print_separator


load_dotenv(dotenv_path='.env')

genai.configure(api_key=os.getenv("GENAI_API_KEY"))


model = genai.GenerativeModel(model_name="gemini-1.5-flash")

while True:
    print_separator()
    request = input("User: ")
    response = model.generate_content(request)

    print_separator()
    print(f"Gemini: {response.text}")
