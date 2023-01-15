import plexapi.exceptions
from src.settings import PLEX_SERVER, PLEX_USERNAME, PLEX_PASSWORD
from plexapi.myplex import MyPlexAccount
from src.logger import logger

account = MyPlexAccount(PLEX_USERNAME, PLEX_PASSWORD)


class Library:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def update(self):
        plex_status().library.section(self.name).update()
        logger.info(f'Plex library {self.name} is updated')


def plex_status():
    """Проверка статуса плекс сервера"""
    try:
        plex = account.resource(PLEX_SERVER).connect()
        return plex
    except plexapi.exceptions.NotFound:
        logger.error(f'Plex connection-DOWN')
        return False


def plex_libraries():
    """Получение всех библиотек плекса и заполенение списка"""
    all_libraries = []
    for elem in plex_status().library.sections():
        library = Library(
            name=elem.title,
            path=''.join(elem.locations)
        )
        all_libraries.append(library)
    logger.info(f'Plex libraries is load')
    return all_libraries

