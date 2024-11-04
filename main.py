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

    prompt_generator.init_info(
        "Київський Політехнічний Університет",
        "4",
        "Інженерія Програмного Забезпечення",
        "реферат",
        "Архітектура інтернет аукціонів"
    )

    print(prompt_generator.document_prompt)

    response = model.generate_content(prompt_generator.document_prompt)

    print_separator()
    print(prompt_generator.response)

    write_usage(os.getenv("USAGE_FILE"), f"## Prompt:\n> {prompt_generator.document_prompt}\n\n"
                                         f"{prompt_generator.response}")


if __name__ == "__main__":
    main()
