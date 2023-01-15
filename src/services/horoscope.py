import requests
from bs4 import BeautifulSoup

from src.bot import bot
from src.settings import URL_HOROSCOPE
from src.logger import logger


def get_horoscope():
    """Парсинг URL_HOROSCOPE и возврат гороскопа"""
    req = requests.get(URL_HOROSCOPE)
    soup = BeautifulSoup(req.text, 'html.parser')
    horoscope = soup.find(
        'div', class_='content_wrapper'
    ).select_one('p').get_text()
    logger.info(f'Horoscope received')
    return horoscope


async def send_horoscope(user_id):
    await bot.send_message(user_id, get_horoscope())
    logger.info(f'Send horoscope to {user_id}')
