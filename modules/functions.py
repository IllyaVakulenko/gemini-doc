import json


def print_separator(symbol="=", length=20):
    print(symbol * length)


def load_templates(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        templates = json.load(file)
    return templates
