import requests
from bs4 import BeautifulSoup

from main import ADMIN_ID, bot


async def send_horoscope():
    req = requests.get('https://goroskop365.ru/aries/')
    soup = BeautifulSoup(req.text, "html.parser")
    wrapper = soup.find('div', class_='content_wrapper')
    horoscope = wrapper.select_one('p').get_text()
    await bot.send_message(ADMIN_ID, horoscope)
