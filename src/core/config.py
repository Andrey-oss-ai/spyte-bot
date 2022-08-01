from pathlib import Path

from dotenv import dotenv_values

env = dotenv_values()


def get_all_users():
    users = env.get('USERS_ID').split(',')
    users.append(env.get('ADMIN_ID'))
    return users


TOKEN = env.get('TELEGRAM_TOKEN')
ADMIN_ID = env.get('ADMIN_ID')
USERS_ID = [int(x) for x in get_all_users()]
URL_WEATHER = env.get('URL_WEATHER')
URL_HOROSCOPE = env.get('URL_HOROSCOPE')
URL_STEAM = env.get('URL_STEAM')
FILES_FOLDER = Path(Path.cwd(), 'files')
DB_FOLDER = Path(Path.cwd(), 'db')
LOG_FOLDER = Path(Path.cwd(), 'logs')
