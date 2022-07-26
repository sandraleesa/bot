import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot

async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text='OK')


async def new_week():
    await bot.send_message(chat_id=chat_id, text='Are you ready for a new week, honey?')


async def reset_routine():
    photo = open('media/reset-routine.png.webp')
    await bot.send_photo(chat_id=chat_id, photo=photo, caption='Good morning!')


async def scheduler():
    aioschedule.every().sunday.at('21:00').do(new_week())
    aioschedule.every().sunday.at('8:00').do(reset_routine())

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda  word:'remind' in word.text)