# Import necessary modules
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

# Load environment variables from .env file
load_dotenv()

# Get the Telegram Bot API token from the environment variables
TOKEN = os.getenv('TOKEN')

# Create an instance of the MemoryStorage for handling conversation states
storage = MemoryStorage()

# Create a Bot instance with the provided token
bot = Bot(token=TOKEN)

# Create a Dispatcher instance that will handle the bot's updates and route them to the appropriate handlers
dp = Dispatcher(bot=bot, storage=storage)
