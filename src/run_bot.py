from aiogram import executor

import handlers # noqa
import middlewares  # noqa
from src.bot import dp

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=handlers.send_on_startup)
