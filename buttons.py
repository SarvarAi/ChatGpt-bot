from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext


def start_chatting():
    keyboard = InlineKeyboardMarkup()
    lets_begin = InlineKeyboardButton(text="let's begin🔥", callback_data='start')
    keyboard.add(lets_begin)
    return keyboard


def stop_chatting_ai():
    keyboard = InlineKeyboardMarkup()
    stop = InlineKeyboardButton(text='🤚Stop', callback_data='stop')
    keyboard.row(stop)
    return keyboard
