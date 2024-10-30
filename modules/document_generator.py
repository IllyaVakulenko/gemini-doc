class PromptGenerator:
    def __init__(self):
        self.user_info = {}
        self.document_info = {}
        self.block = ""
        self.hint = False
        self.document_prompt = ""

    def add_hint_text(self, hint_text):
        return hint_text if self.hint else ''

    def get_user_info(self):
        self.user_info = {
            "education": input(f"Місце навчання{self.add_hint_text(' (наприклад, \"фаховий музичний коледж\")')}: "),
            "course": input(f"Курс{self.add_hint_text(' (наприклад, \"4\")')}: "),
            "specialization": input(
                f"Спеціальність{self.add_hint_text(' (наприклад, \"Оркестрові духові та ударні інструменти\")')}: ")
        }

    def get_document_info(self):
        self.document_info = {
            "document_type": input(f"Тип документа{self.add_hint_text(' наприклад, \"доповідь\", \"есе\", \"дослідницька робота\"')}: "),
            "topic": input(f"Тема документа{self.add_hint_text(' наприклад, \"Домашня робота як фактор самовиховання\"')}: ")
        }

    def generate_block_info(self):
        self.block = input(f"Назва блоку для розкриття{self.add_hint_text(' (наприклад, \"Поняття самовиховання\")')}: ")

    def generate_document_prompt(self):
        intro_template = "Ти студент {{user_info.education}}, курс {{user_info.course}}, спеціальність {{user_info.specialization}}."
        prompt_template = "Напиши структуру {{document_type}} на тему: \"{{topic}}\""

        intro = intro_template.replace("{{user_info.education}}", self.user_info["education"]) \
            .replace("{{user_info.course}}", self.user_info["course"]) \
            .replace("{{user_info.specialization}}", self.user_info["specialization"])

        prompt = prompt_template.replace("{{document_type}}", self.document_info["document_type"]) \
            .replace("{{topic}}", self.document_info["topic"])

        return f"{intro} {prompt}"

    def generate_block_prompt(self):
        prompt_template = "Розпиши {{block}}"

        # Заповнення шаблону
        return prompt_template.replace("{{block}}", self.block)

    def enable_hint(self):
        self.hint = True

    def disable_hint(self):
        self.hint = False

    def run(self):
        self.get_user_info()
        self.get_document_info()

        document_prompt = self.generate_document_prompt()

        print("\nЗгенерований запит для структури документа:")
        # print(document_prompt)

        return document_prompt
