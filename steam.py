import pickle

import requests
from bs4 import BeautifulSoup as BS

from main import ADMIN_ID, ROOT_DIR, bot

URL = 'https://playisgame.com/halyava/steam'

FILE = f'{ROOT_DIR}/steam_data.pickle'


def parse_site():
    page = requests.get(URL)
    CODE: int = page.status_code
    if CODE == 200:
        html = BS(page.content, 'html.parser')
        items = html.find_all(class_='pp-post-wrap pp-grid-item-wrap')
        records = {}
        for elem in items:
            text = elem.find(class_="pp-post-title").find('a').get_text()
            link = elem.find(class_="pp-post-title").find('a').get('href')
            img_link = elem.find(class_='pp-post-thumbnail-wrap').find('img')['src']
            records[text] = {'link': link, 'img': img_link}
        return records


def create_file():
    with open(FILE, 'wb') as f:
        pickle.dump(parse_site(), f)


def read_file():
    with open(FILE, 'rb') as f:
        saved_records = pickle.load(f)
        return saved_records


async def send_steam_news():
    all_records = parse_site()
    try:
        new_items = set(all_records) - set(read_file())
    except FileNotFoundError:
        create_file()
        new_items = set(all_records) - set(read_file())
    for item in new_items:
        img_link = all_records[item]['img']
        link = all_records[item]['link']
        href = f'<a href="{link}">{item}</a>'

        await bot.answer(
            ADMIN_ID,
            photo=img_link,
            caption=href,
            parse_mode='HTML'
        )
    create_file()
