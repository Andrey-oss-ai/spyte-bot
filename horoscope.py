import requests
from bs4 import BeautifulSoup


async def send_horoscope(msg):
    req = requests.get('https://goroskop365.ru/aries/')
    soup = BeautifulSoup(req.text, "html.parser")
    horoscope = soup.find('div', class_='content_wrapper').select_one('p').get_text()
    await msg.answer(horoscope)