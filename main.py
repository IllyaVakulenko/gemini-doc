import google.generativeai as genai
import os
from dotenv import load_dotenv
from modules.functions import *
from modules.document_generator import PromptGenerator


load_dotenv(dotenv_path='.env')

genai.configure(api_key=os.getenv("GENAI_API_KEY"))

prompt_generator = PromptGenerator()

model = genai.GenerativeModel(model_name="gemini-1.5-flash")


def main():
    print_separator()

    # prompt_generator.write_info()
    prompt_generator.init_info(
        "Київський Політехнічний Університет",
        "4",
        "Інженерія Програмного Забезпечення",
        "реферат",
        "Архітектура інтернет аукціонів"
    )

    print(prompt_generator.document_prompt)

    # request = input("User: ")
    response = model.generate_content(prompt_generator.document_prompt)

    print_separator()
    print(response.text)


if __name__ == "__main__":
    main()
