import requests
from bs4 import BeautifulSoup
from columnar import columnar

URL = 'https://yandex.ru/pogoda/moscow/details'
TABLE = 'weather-table'
BODY = f'{TABLE}__body-cell'

async def send_weather(msg):
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, 'html.parser')
    weather_block = soup.find(class_=f'{TABLE}__body').find_all(class_=f'{TABLE}__row')
    data = []
    for elem in weather_block:
        time = elem.find(class_=f'{TABLE}__daypart').text
        temperature = elem.find(class_=f'{TABLE}__temp').text.replace('…', ' ')
        precipitation = elem.find(class_=f'{BODY}_type_condition').text
        humidity = elem.find(class_=f'{BODY}_type_humidity').text
        wind = elem.find(class_='wind-speed').text
        real = elem.find(class_=f'{BODY}_type_feels-like').text
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
    await msg.answer(weather)
    