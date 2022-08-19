import sys
from aiogram import executor
import asyncio
import aioschedule as schedule
import handlers  # noqa
import middlewares  # noqa
from src import dp
from services import send_finished_torents

sys.path.append('../')


async def scheduler():
    schedule.every(1).minutes.do(send_finished_torents)
    while True:
        await schedule.run_pending()
        await asyncio.sleep(2)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    asyncio.ensure_future(scheduler())
    executor.start_polling(
        dp,
        skip_updates=True,
        on_startup=handlers.send_on_startup
    )
