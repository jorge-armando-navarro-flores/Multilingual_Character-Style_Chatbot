from chains import multilingual_character_chain
from options import characters, languages


def respond(message, chat_history, character, language):
    chat_history.append({"role": "user", "content": message})
    response = multilingual_character_chain.invoke(
        {"messages": chat_history, "character": character, "language": language}
    )
    chat_history.append({"role": "assistant", "content": response})

    return response


def get_characters():
    return characters


def get_languages():
    return languages
