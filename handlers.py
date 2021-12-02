from aiogram.types import Message
from horoscope import send_horoscope
from weather import send_weather
from main import bot, dp


@dp.message_handler()
async def send_messages(msg: Message):
    if msg.text.lower() == "horoscope":
        await send_horoscope(msg)
    if msg.text.lower() == "weather":
        await send_weather(msg)