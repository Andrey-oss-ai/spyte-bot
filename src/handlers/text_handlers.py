from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from src.core import ADMIN_ID
from src.bot import dp, bot
from src.services import get_horoscope, get_weather, send_steam_news


async def send_on_startup(*args):
    await bot.send_message(ADMIN_ID, "Raspberry started")


@dp.message_handler(Text(equals=['horoscope'], ignore_case=True))
async def horoscope_handler(message: Message):
    await message.answer(get_horoscope())


@dp.message_handler(Text(equals=['weather'], ignore_case=True))
async def weather_handler(message: Message):
    await message.answer(get_weather())


@dp.message_handler(Text(equals=['steam'], ignore_case=True))
async def steam_handler(message: Message):
    await send_steam_news()
