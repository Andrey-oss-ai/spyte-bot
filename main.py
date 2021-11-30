import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    executor.start_polling(dp)