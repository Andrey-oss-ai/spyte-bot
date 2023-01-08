from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from src import bot, dp
from src.settings import ADMIN_ID, torrent_status, plex_status
from src.services import get_horoscope, get_weather, send_steam_news


async def send_on_startup(*args):
    await bot.send_message(ADMIN_ID, f'Raspberry started\n'
                                     f'Torrent status - {torrent_status()}\n'
                                     f'Plex status - {plex_status()}', parse_mode='HTML')


@dp.message_handler(Text(equals=['horoscope'], ignore_case=True))
async def horoscope_handler(message: Message):
    await message.answer(get_horoscope())


@dp.message_handler(Text(equals=['weather'], ignore_case=True))
async def weather_handler(message: Message):
    await message.answer(get_weather())


@dp.message_handler(Text(equals=['steam'], ignore_case=True))
async def steam_handler(message: Message):
    await send_steam_news(answer=True)
