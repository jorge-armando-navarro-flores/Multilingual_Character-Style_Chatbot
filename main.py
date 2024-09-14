import gradio as gr
from app import set_chain, respond, get_characters, get_languages

characters = get_characters()
languages = get_languages()

with gr.Blocks() as demo:
    start_character = characters[0]
    start_language = languages[0]
    set_chain(start_character, start_language)

    with gr.Row():
        with gr.Column(scale=1):
            character_dropdown = gr.Dropdown(
                label="Character Selection",
                value=start_character,
                choices=characters,
            )
            language_dropdown = gr.Dropdown(
                label="langauge Selection",
                value=start_language,
                choices=languages,
            )
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(type="messages")
            gr.ChatInterface(
                fn=respond,
                chatbot=chatbot,
                type="messages",
            )

    character_dropdown.input(
        set_chain, inputs=[character_dropdown, language_dropdown], outputs=[chatbot]
    )

    language_dropdown.input(
        set_chain, inputs=[character_dropdown, language_dropdown], outputs=[chatbot]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
