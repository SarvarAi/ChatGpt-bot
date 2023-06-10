from aiogram import executor
from loader import dp

# Starting the main.py where is the all script of the bot
import main

if __name__ == '__main__':
    # Start the polling process, passing the dispatcher object
    executor.start_polling(dispatcher=dp)
