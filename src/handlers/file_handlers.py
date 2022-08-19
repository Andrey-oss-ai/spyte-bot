from pathlib import Path

from src import bot, dp
from src.core import FILES_FOLDER
from src.core.loging import logger


async def file_saved(message, filename):
    await message.answer(f'Файл <u>{filename}</u> сохранен', parse_mode='HTML')
    logger.info(f'File saved at {filename}')


@dp.message_handler(content_types=['photo'])
async def file_image(message):
    filename = f'{message.message_id}.jpg'
    await message.photo[-1].download(
        destination_file=Path(FILES_FOLDER, filename)
    )
    await file_saved(message, filename)


@dp.message_handler(content_types=['video'])
async def file_video(message):
    filename = f'{message.message_id}.mp4'
    file = await bot.get_file(message.video.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, Path(FILES_FOLDER, filename))
    await file_saved(message, filename)


@dp.message_handler(content_types=['document'])
async def file_doc(message):
    filename = f'{message.document.file_name}'
    file = await bot.get_file(message.document.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, Path(FILES_FOLDER, filename))
    await file_saved(message, filename)


@dp.message_handler(content_types=['voice'])
async def file_voice(message):
    filename = f'{message.message_id}.ogg'
    file = await bot.get_file(message.voice.file_id)
    file_path = file.file_path
    await bot.download_file(file_path, Path(FILES_FOLDER, filename))
    await file_saved(message, filename)


@dp.message_handler(content_types=['audio'])
async def file_audio(message):
    m_type = str(message.audio.mime_type)
    extension = m_type[m_type.find('/') + 1:len(m_type)]
    file = await bot.get_file(message.audio.file_id)
    file_path = file.file_path
    if message.audio.performer != '<unknown>':
        filename = f'{message.audio.performer}-{message.audio.title}.{extension}'
    else:
        filename = f'{message.audio.title}.{extension}'
    await bot.download_file(file_path, Path(FILES_FOLDER, filename))
    await file_saved(message, filename)
