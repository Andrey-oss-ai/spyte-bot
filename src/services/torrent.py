from src.settings import ADMIN_ID
from .plex import plex_libraries, plex_status
from src.bot import bot
from src.settings import URL_TORRENT_SERV
from qbittorrent import Client
from src.logger import logger
import requests

finish_statuses = ['stalledUP', 'uploading']


class Torrent:
    def __init__(self, name, status, progress, path, hash):
        self.name = name
        self.status = status
        self.progress = progress
        self.path = path
        self.hash = hash

        if self.status in finish_statuses:
            logger.info(f'download {name} completed')

    def delete(self):
        torrent_connect().delete(self.hash)
        logger.info(f'Torrent {self.name} deleted')


def torrent_status():
    try:
        response = requests.head(URL_TORRENT_SERV)
        if response.status_code == 200:
            return True
        else:
            logger.error(f'Torrent connection-DOWN')
            return False
    except Exception:
        logger.error(f'Torrent connection-DOWN')
        return False


def torrent_connect():
    qb = Client(URL_TORRENT_SERV)
    return qb


def get_torrents():
    """Получение всех торрентов"""
    torrents = []
    for elem in torrent_connect().torrents():
        torrent = Torrent(
            elem['name'],
            elem['state'],
            f'{round(elem["progress"] * 100)}%',
            elem['save_path'][:-1], elem['hash']
        )
        logger.info(f'Load {torrent.name} torrent {torrent.progress}')
        torrents.append(torrent)
    return torrents


async def send_finished_torrents():
    """Если завершенный торрент скачивался в библиокеку plex то запуск обновления библеотеки и удаление торрента"""
    if torrent_status():
        for torrent in get_torrents():
            if torrent.status in finish_statuses:
                await bot.send_message(ADMIN_ID, f'Скачивание {torrent.name} завершено')
                if plex_status():
                    for library in plex_libraries():
                        if torrent.path == library.path:
                            library.update()
                            await bot.send_message(ADMIN_ID, f'Библиотека {library} обновлена')
                    torrent.delete()
                    await bot.send_message(ADMIN_ID, f'Торрент {torrent.name} удален')
