import google.generativeai as genai
import os
from dotenv import load_dotenv
from modules.functions import *
from modules.document_generator import PromptGenerator


load_dotenv(dotenv_path='.env')

genai.configure(api_key=os.getenv("GENAI_API_KEY"))

prompt_generator = PromptGenerator()

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

while True:
    print_separator()

    prompt_generator.run()


    # request = input("User: ")
    # response = model.generate_content(request)

    # print_separator()
    # print(f"Gemini: {response.text}")
