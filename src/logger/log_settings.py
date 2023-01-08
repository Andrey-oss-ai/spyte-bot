from loguru import logger

from src.settings import LOG_FOLDER

LOG_FOLDER.mkdir(exist_ok=True)

format_log = '{time:DD:MM:YYYY HH:mm:ss} {level} {message}'

logger.add('logs/logs.log', format=format_log)

new_level = logger.level('SPAM', no=38, color='<red>')
