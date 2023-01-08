from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from src.settings import USERS_ID
from src.logger import logger


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user
        elif update.callback_query:
            user = update.callback_query.from_user
        else:
            return
        if user.id not in USERS_ID:
            logger.log(
                'SPAM',
                f'Message "{update.message.text}" from {user.full_name} {user.id}'
            )
            raise CancelHandler

    async def on_pre_process_message(self, message: types.message, data: dict):
        msg_type = message.content_type
        media_types = ['photo', 'video', 'document', 'voice', 'audio']
        if msg_type == 'text':
            logger.info(
                f'Incoming message "{message.text}" '
                f'from {message.from_user.full_name} '
                f'id - {message.from_user.id}'
            )
        elif msg_type in media_types:
            logger.info(f'Incoming file: {msg_type} '
                        f'from {message.from_user.full_name} '
                        f'id - {message.from_user.id}'
                        )
