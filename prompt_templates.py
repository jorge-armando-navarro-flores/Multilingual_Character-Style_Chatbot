def character_prompt_template(character, language):
    return [
        {
            "role": "system",
            "content": f"You are an assistant that speaks like {character}.",
        },
        {
            "role": "system",
            "content": f"Translate all your answers to {language} language",
        },
    ]