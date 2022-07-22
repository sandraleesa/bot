from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from database.bot_db import sql_command_random


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Hello and nice to meet you {message.from_user.full_name}')


async def quiz_handler(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton('Next question', callback_data='button_call_1')
    markup.add(button_call_1)

    question = 'Who is BoJack?'
    answer = [
        'Singer',
        'Host on a TV Show',
        'Horseman obviously',
        'Alcoholic and drug addict'
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="It is obvious",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup
    )


async def meme_handler(message: types.message):
    photo = open('media/maxresdefault.jpg', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


async def pin_handler(message: types.Message):
    if not message.reply_to_message:
        await message.answer('The command must be a reply for the message')
    else:
        await bot.pin_chat_message(message.chat.id, message.reply_to_message.from_user.id)


async def dice_handler(message: types.Message):
    dice_player = await bot.send_dice(message.chat.id, emoji='🎲')
    dice_bot = await bot.send_dice(message.chat.id, emoji='🎲')
    if dice_player.dice.value > dice_bot.dice.value:
        await bot.send_message(message.chat.id, f'You won!')
    elif dice_player.dice.value < dice_bot.dice.value:
        await bot.send_message(message.chat.id, f'You lost!')
    else:
        await bot.send_message(message.chat.id, f'Same score!')


async def show_random_dish(message: types.Message):
    await sql_command_random(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(quiz_handler, commands=['quiz'])
    dp.register_message_handler(meme_handler, commands=['meme'])
    dp.register_message_handler(pin_handler, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(dice_handler, commands=['dice'])
    dp.register_message_handler(show_random_dish, commands=['random'])
