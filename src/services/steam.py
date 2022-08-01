import requests
from bs4 import BeautifulSoup
from sqlalchemy import select

from src.bot import bot
from src.core import ADMIN_ID, URL_STEAM, Game, db_connect
from src.core.loging import logger

session = db_connect()


def parse_site():
    page = requests.get(URL_STEAM)
    html = BeautifulSoup(page.content, 'html.parser')
    items = html.find_all(class_='pp-post-wrap pp-grid-item-wrap')
    for elem in items:
        element = elem.find(class_='pp-post-title').find('a')
        text = element.get_text()
        link = element.get('href')
        image = elem.find(class_='pp-post-thumbnail-wrap')
        img_link = image.find('img')['src']
        find = session.query(Game).where(Game.link == link)
        if not session.query(find.exists()).scalar():
            session.add(
                Game(
                    link=link,
                    image=img_link,
                    text=text,
                )
            )
            session.commit()


async def send_steam_news():
    parse_site()
    result = session.execute(
        select(Game).where(Game.send == False)
    ).scalars().all()
    if not len(result):
        await bot.send_message(ADMIN_ID, 'Новостей нет')
        logger.info('No news to send')
    else:
        for elem in result:
            elem.send = True
            session.commit()
            await bot.send_photo(
                ADMIN_ID,
                photo=elem.link,
                caption=f'<a href="{elem.link}">{elem.text}</a>',
                parse_mode='HTML'
            )
    logger.info(f'Send {len(result)} news to {ADMIN_ID}')
