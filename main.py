import os

from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from dotenv import load_dotenv

from loader import dp, bot
from buttons import start_chatting, stop_chatting_ai
from ai import AI

load_dotenv()
OWNER_ID = os.getenv('OWNER_ID')


class ChatState(StatesGroup):
    message = State()


@dp.message_handler(commands=['start'])
async def start(message: Message):
    user_id = message.chat.id
    if str(user_id) == OWNER_ID:
        # Send the start message and display the "start_chatting" button
        await message.answer(f'Lets start chatting! Write your question',
                             reply_markup=start_chatting())


@dp.callback_query_handler(lambda call: call.data == 'start')
async def ai_listening(call: CallbackQuery):
    # Edit the message to indicate that ChatGpt is listening
    await bot.edit_message_text('ChatGpt is listening you👂',
                                chat_id=call.message.chat.id,
                                message_id=call.message.message_id,
                                reply_markup=stop_chatting_ai())

    # Set the state to "message" to wait for the user's message
    await ChatState.message.set()


@dp.callback_query_handler(lambda call: call.data == 'stop', state=ChatState.message)
async def stop_chatting(call: CallbackQuery, state: FSMContext):
    # Send a message to indicate that chatting is stopped
    await call.message.answer('Chatting is stopped now!')

    # Send the start message and display the "start_chatting" button
    await call.message.answer(f'Lets start chatting! Write your question',
                              reply_markup=start_chatting())

    # Finish the state
    await state.finish()


@dp.message_handler(state=ChatState.message)
async def ai_answering(message: Message):
    # Create an AI instance with the user's message
    ai = AI(message=message.text)

    # Get the AI's response and send it as a message
    await message.answer(ai.operate(), reply_markup=stop_chatting_ai())