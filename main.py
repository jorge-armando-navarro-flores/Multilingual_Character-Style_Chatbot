import gradio as gr
from app import get_answer, get_character_prompt, get_characters, get_languages

def respond(message, chat_history):
        chat_history.append({"role": "user", "content": message})
        response = get_answer(chat_history)
        chat_history.append({"role": "assistant", "content": response})
        return response

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=1):
            character_dropdown = gr.Dropdown(
                label="Character Selection",
                value="William Shakespeare",
                choices=get_characters(),
            )
            language_dropdown = gr.Dropdown(
                label="langauge Selection", value="English", choices=get_languages()
            )
        with gr.Column(scale=3):
                chatbot = gr.Chatbot(
                    get_character_prompt("William Shakespeare", "English"), type="messages"
                )
                gr.ChatInterface(fn=respond, chatbot=chatbot, type="messages", retry_btn=None, undo_btn=None, clear_btn=None)

    
    character_dropdown.input(
        get_character_prompt,
        inputs=[character_dropdown, language_dropdown],
        outputs=[chatbot],
    )

    language_dropdown.input(
        get_character_prompt,
        inputs=[character_dropdown, language_dropdown],
        outputs=[chatbot],
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
