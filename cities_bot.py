import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import Dispatcher, filters
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


logging.basicConfig(level=logging.INFO)
TOKEN='Вставьте токен вашего бота'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

cities_db = []
with open('cities_db.txt', 'r', encoding="utf8") as file:
    for line in file:
        cities_db.append(line.rstrip().lower())

last_letter = ""
last_letter_bot = ""
cities = []

button1 = KeyboardButton('Начать заново', callback_data='try_again')

markup3 = ReplyKeyboardMarkup().add(button1)


@dp.message_handler(commands=['begin'])
async def start(callback_query: types.CallbackQuery):
    username = callback_query.from_user.username

    await bot.send_message(
        callback_query.from_user.id,
        text='Добро пожаловать в игру города',
        # reply_markup=reply_keyboard,
    )

@dp.message_handler(commands=['start'])
async def start(callback_query: types.CallbackQuery):
    username = callback_query.from_user.username

    await bot.send_message(
        callback_query.from_user.id,
        text='Добро пожаловать в игру города\nДля продолжения введите название города',
        # reply_markup=reply_keyboard,
    )




executor.start_polling(dp, skip_updates=True)
