from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

parser = StrOutputParser()
model = ChatOpenAI(model="gpt-3.5-turbo")


class Chain:
    def __init__(self, character, language):
        self.set_multilingual_character_chain(character, language)

    def set_multilingual_character_chain(self, character, language):

        prompt_template = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    f"You are an assistant that speaks like {character}.",
                ),
                (
                    "system",
                    f"Translate all your answers to {language} language.",
                ),
                MessagesPlaceholder(variable_name="messages"),
            ]
        )

        self.chain = prompt_template | model | parser

    def get_chain(self):
        return self.chain
