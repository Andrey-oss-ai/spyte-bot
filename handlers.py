from aiogram.types import Message

from main import bot, dp


@dp.message_handler()
async def send_messages(msg: Message):
    await msg.answer(msg.text)