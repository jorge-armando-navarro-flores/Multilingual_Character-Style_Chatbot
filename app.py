from openai_service import get_chain
from prompt_templates import character_prompt_template
from options import characters, languages


def get_answer(messages):
    response = get_chain().invoke(messages)
    return response


def get_character_prompt(character, language):
    return character_prompt_template(character, language)


def get_characters():
    return characters


def get_languages():
    return languages
