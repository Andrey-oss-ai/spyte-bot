import requests
from bs4 import BeautifulSoup

from src.bot import bot
from src.core import ADMIN_ID, URL_HOROSCOPE
from src.core.loging import logger


def get_horoscope():
    req = requests.get(URL_HOROSCOPE)
    soup = BeautifulSoup(req.text, 'html.parser')
    horoscope = soup.find(
        'div', class_='content_wrapper'
    ).select_one('p').get_text()
    return horoscope


async def send_horoscope():
    await bot.send_message(ADMIN_ID, get_horoscope())
    logger.info(f'Send horoscope to {ADMIN_ID}')
