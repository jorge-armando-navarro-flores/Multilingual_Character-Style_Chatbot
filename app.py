from chains import Chain
from options import characters, languages

chain = Chain(characters[0], languages[0])


def set_chain(character, language):
    chain.set_multilingual_character_chain(character, language)


def get_answer(messages):
    response = chain.get_chain().invoke({"messages": messages})
    return response


def respond(message, chat_history):
    chat_history.append({"role": "user", "content": message})
    response = get_answer(chat_history)
    chat_history.append({"role": "assistant", "content": response})

    return response


def get_characters():
    return characters


def get_languages():
    return languages
