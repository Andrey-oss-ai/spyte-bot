import sys

sys.path.append('./')
sys.path.append('/')
from aiogram import executor
import handlers  # noqa
from src import dp
from services import send_finished_torrents
from apscheduler.schedulers.asyncio import AsyncIOScheduler

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')


def add_schedulers_jobs():
    scheduler.add_job(send_finished_torrents, 'interval', seconds=30)
    #   scheduler.add_job(get_weather, 'cron', day_of_week='mon-sun', hour=09, minute=00, end_date='2025-10-13')


if __name__ == '__main__':
    add_schedulers_jobs()
    scheduler.start()
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=handlers.send_on_startup
    )
