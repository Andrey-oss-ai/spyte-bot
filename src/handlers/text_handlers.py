from aiogram.dispatcher.filters import Text
from aiogram.types import Message

from src import bot, dp
from src.settings import ADMIN_ID
from src.services import send_horoscope, send_weather, send_steam_news, plex_status, torrent_status


async def send_on_startup(*args):
    await bot.send_message(ADMIN_ID, f'Raspberry started\n'
                                     f'Torrent status - {"ОК" if torrent_status() else "Down"}\n'
                                     f'Plex status - {"ОК" if plex_status() else "Down"}', parse_mode='HTML')


@dp.message_handler(Text(equals=['horoscope'], ignore_case=True))
async def horoscope_handler(message: Message):
    await send_horoscope(message.from_user.id)


@dp.message_handler(Text(equals=['weather'], ignore_case=True))
async def weather_handler(message: Message):
    await send_weather(message.from_user.id)


@dp.message_handler(Text(equals=['steam'], ignore_case=True))
async def steam_handler(message: Message):
    await send_steam_news(answer=True)
