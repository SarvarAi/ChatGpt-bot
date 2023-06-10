import os

import openai
from dotenv import load_dotenv


class AI:
    """Class AI is fully responsible for AI part of the bot"""
    def __init__(self, message):
        # Load environment variables from .env file
        load_dotenv()

        # Get the OpenAI API key from the environment variables
        self.OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

        # Set the model to use
        self.model = 'gpt-3.5-turbo'

        # Store the message
        self.message = message

    def _get_answer(self):
        # Create a chat completion request to OpenAI API
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    'role': 'user',
                    'content': self.message
                }
            ]
        )

        # Get the generated answer from the completion response
        answer = completion.choices[0].message
        return answer

    def operate(self):
        # Get the answer from OpenAI API and return it as a string
        return str(self._get_answer())
