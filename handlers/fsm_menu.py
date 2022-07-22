from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMIN
from keyboards import client_kb
from database import bot_db


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def fsm_start(message: types.Message):
    if message.from_user.id in ADMIN:
        await FSMAdmin.photo.set()
        await message.answer(f"Hello {message.from_user.full_name}!Let's add the dish!"
                             f"Send photo of the dish", reply_markup=client_kb.cancel_markup)
    else:
        await message.reply("You are not an ADMIN!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("What is the name of the dish?")


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await FSMAdmin.next()
    await message.answer("Describe the dish")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await FSMAdmin.next()
    await message.answer("What is the price for the dish?")


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"Name: {data['name']}\n"
                                     f"Description: {data['description']}\n"
                                     f"Price: {data['price']}\n")
    await state.finish()
    await message.answer("The dish is successfully added")


async def cancel_registration(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    else:
        await state.finish()
        await message.answer("Adding of the dish is cancelled!")


async def delete_data(message: types.Message):
        if message.from_user.id in ADMIN and message.chat.type == 'private':
            dishes = await bot_db.sql_command_all()
            for dish in dishes:
                await bot.send_photo(message.from_user.id, dish[2],
                                     caption=f"Name: {dish[3]}\n"
                                             f"Description: {dish[4]}\n"
                                             f"Prive: {dish[5]}\n"
                                             f"{dish[1]}",
                                     reply_markup=InlineKeyboardMarkup().add(
                                         InlineKeyboardButton(
                                             f'delete {dish[3]}',
                                             callback_data=f'delete {dish[0]}'
                                         )
                                     ))
        else:
            await message.reply('You are not an ADMIN')


async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace('delete', ''))
    await call.answer(text='The dish is deleted', show_alert=True)
    await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsmmenu(dp: Dispatcher):
    dp.register_message_handler(cancel_registration, state="*", commands='cancel')
    dp.register_message_handler(cancel_registration,
                                Text(equals='cancel', ignore_case=True), state="*")

    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith('delete')
                                       )
