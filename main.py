import asyncio
import os

import aioschedule as schedule
from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')


async def scheduler():
    schedule.every().day.at('09:00').do(send_horoscope)
    schedule.every().day.at('09:00').do(send_weather)
    schedule.every().hour.do(send_steam_news)

    while True:
        await schedule.run_pending()
        await asyncio.sleep(2)


bot = Bot(TOKEN)
dp = Dispatcher(bot)

if __name__ == '__main__':
    from handlers import dp

    loop = asyncio.get_event_loop()
    asyncio.ensure_future(scheduler())
    from horoscope import send_horoscope
    from steam import send_steam_news
    from weather import send_weather

    executor.start_polling(dp)
