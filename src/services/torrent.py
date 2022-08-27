from src.core import ADMIN_ID, get_torrents, plex_library, plex_update, torrent_connect, torrent_status
from src.bot import bot


async def send_finished_torents():
    if torrent_status():
        for elem in get_torrents():
            if get_torrents()[elem]['state'] == 'finished':
                await bot.send_message(ADMIN_ID, f'Скачивание {elem} завершено')
                for library in plex_library():
                    if get_torrents()[elem]['state'] in library.values():
                        plex_update(library)
                        await bot.send_message(ADMIN_ID, f'Библиотека {library} обновлена')
                torrent_connect().delete(get_torrents()[elem]['hash'])
                await bot.send_message(ADMIN_ID, f'Торрент {elem} удален')
