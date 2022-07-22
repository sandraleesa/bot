from aiogram import types, Dispatcher
from config import bot, ADMIN, dp


async def echo(message: types.Message):
    if message == int:
        await bot.send_message(message.from_user.id, message.text)
    else:
        await bot.send_message(message.from_user.id, message.text*message.text)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo)


