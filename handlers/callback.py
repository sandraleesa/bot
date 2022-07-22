from aiogram import types, Dispatcher
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode


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
        reply_markup=markup,
    )


async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton('Next', callback_data='button_call_3')
    markup.add(button_call_3)

    question = 'What or who was Cowboy Bebop?'
    answer = [
        'Spaceship of Spike Spiegel',
        'Popular western movie',
        'The first ever cowboy',
        'Song of the Beatles',
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation="Look up my name",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


async def quiz_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton('Next', callback_data='button_call_4')
    markup.add(button_call_4)

    question = 'When do we wear pink?'
    answer = [
        'Everyday',
        'On Wednesdays we wear pink!',
        'We dont wear pink',
        'Every other day',
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="Look up my name",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2,
                                       lambda call: call.data == 'button_call_1')
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == 'button_call_2')
    dp.register_callback_query_handler(quiz_4,
                                       lambda call: call.data == 'button_call_3')