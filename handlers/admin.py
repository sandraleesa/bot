from aiogram import types, Dispatcher
from config import bot, ADMIN, dp
import random
from database.bot_db import sql_commands_get_all_id


async def game(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMIN:
            await message.answer('You are not an ADMIN!')
        elif message.text.startswith('game'):
            emojis = ['⚽', '🏀', '🎳', '🎲', '🎰', '🎯']
            await bot.send_message(f'{(random.choice(emojis))}')


async def reklama(message:types.Message):
    if message.from_user.id in ADMIN:
        result = await sql_commands_get_all_id()
        for id in result:
            await bot.send_message(id[0], message.text[3:])
    else:
        await message.answer('You are not an ADMIN')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game)
    dp.register_message_handler(reklama, commands=['reklama'])
