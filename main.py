from aiogram import types
from aiogram.utils import executor
from aiogram.types import ParseMode, InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp
import logging


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'Hello and nice to meet you {message.from_user.full_name}')


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(lambda call: call.data == 'button_call_1')
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Next', callback_data='button_call_2')
    markup.add(button_call_2)

    question = 'Who is Elliot Alderson?'
    answer = [
        'Famous geologist',
        'Painter from NewYork',
        'Sociopath',
        'Genius revolutioner hacker',
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="He is Mr Robot",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


@dp.message_handler(commands=['meme'])
async def meme_handler(message: types.message):
    photo = open('media/maxresdefault.jpg', 'rb')
    await bot.send_photo(chat_id=message.chat.id, photo=photo)


@dp.message_handler()
async def echo(message: types.Message):
    if type(message) == int:
        await bot.send_message(message.from_user.id, message.text * message.text)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
