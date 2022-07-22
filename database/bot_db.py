import sqlite3
from config import bot
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect('bot_sqlite3')
    cursor = db.cursor()

    if db:
        print('Database is connected!')

    db.execute("CREATE TABLE IF NOT EXISTS anketa"
               "(name PRIMARY KEY, photo TEXT, "
               "description TEXT, price INTEGER)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy as data:
        cursor.execute('INSERT INTO menu VALUES'
                       '(?, ?, ?, ?)', tuple(data.values()))
        db.commit()


async def sql_command_random(message):
    result = cursor.execute('SELECT * FROM menu').fetchall()
    random_dish = random.choice(result)
    await bot.send_photo(message.from_user.id, random_dish[2],
                         caption=f"Name: {random_dish[3]}\n"
                                 f"Description: {random_dish[4]}\n"
                                 f"Price: {random_dish[5]}\n"
                                 f"{random_dish[1]}")


async def sql_command_all():
    return cursor.execute('SELECT * FROM menu').fetchall()


async def sql_command_delete(id):
    cursor.execute('DELETE FROM menu WHERE id == ?', (id, ))
    db.commit()


async def sql_commands_get_all_id():
    return cursor.execute('SELECT id FROM menu').fetchall()
