import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv(dotenv_path='.env')

genai.configure(api_key=os.getenv("GENAI_API_KEY"))


model = genai.GenerativeModel(model_name="gemini-1.5-flash")
response = model.generate_content("Hello!")


print(response.text)
