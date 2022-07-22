from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_button = KeyboardButton('/start')
help_button = KeyboardButton('/help')
quiz_button = KeyboardButton('/quiz')
meme_button = KeyboardButton('/meme')
location_button = KeyboardButton('Share location', request_location=True)
info_button = KeyboardButton('Share info', request_contact=True)


cancel_button = KeyboardButton("CANCEL")
cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True,
                                    one_time_keyboard=True).add(cancel_button)
