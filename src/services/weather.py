import requests
from bs4 import BeautifulSoup
from columnar import columnar

from src.bot import bot
from src.settings import ADMIN_ID, URL_WEATHER
from src.logger.log_settings import logger

TABLE = 'weather-table'
BODY = f'{TABLE}__body-cell'


def get_weather():
    req = requests.get(URL_WEATHER)
    soup = BeautifulSoup(req.text, 'html.parser')
    weather_table = soup.find(class_=f'{TABLE}__body')
    weather_block = weather_table.find_all(class_=f'{TABLE}__row')
    data = []
    for elem in weather_block:
        time = elem.find(class_=f'{TABLE}__daypart').text
        temperature = elem.find(class_=f'{TABLE}__temp').text.replace('…', ' ')
        precipitation = elem.find(class_=f'{BODY}_type_condition').text
        humidity = elem.find(class_=f'{BODY}_type_humidity').text
        wind = elem.find(class_='wind-speed').text
        pre_real = elem.find(class_=f'{BODY}_type_feels-like')
        real = pre_real.find(class_='temp__value temp__value_with-unit').text
        data.append(
            [
                time,
                f'{temperature}°',
                precipitation,
                humidity,
                f'{wind}м/с',
                f'{real}°'
            ]
        )

    headers = None
    weather = columnar(data, headers, no_borders=True)
    return weather


async def send_weather():
    await bot.send_message(ADMIN_ID, get_weather())
    logger.info(f'Send weather to {ADMIN_ID}')
