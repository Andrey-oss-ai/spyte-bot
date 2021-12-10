from aiogram.types import Message

from horoscope import send_horoscope
from main import dp
from steam import send_steam_news
from weather import send_weather


@dp.message_handler()
async def send_messages(msg: Message):
    if msg.text.lower() == "horoscope":
        await send_horoscope()
    if msg.text.lower() == "weather":
        await send_weather()
    if msg.text.lower() == "steam":
        await send_steam_news()
