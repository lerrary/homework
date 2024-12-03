from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from crud_functions import *

api = '7631030709:AAGZeT6s0_Fx9Jgr79uJw1Rs1kyjF9nvsQY'
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000

kb1 = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton( text = 'Рассчитать')
button2 = KeyboardButton( text = 'Информация')
button3 = KeyboardButton( text = 'Купить')
button4 = KeyboardButton( text = 'Регистрация')
kb1.add(button1, button2)
kb1.add(button4, button3)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
button5 = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
button6 = InlineKeyboardButton(text = 'Формулы расчёта', callback_data='formulas')
kb2.add(button5, button6)

kb_vit = InlineKeyboardMarkup(resize_keyboard=True)
but_1 = InlineKeyboardButton(text = 'Product1', callback_data='product_buying')
but_2 = InlineKeyboardButton(text = 'Product2', callback_data='product_buying')
but_3 = InlineKeyboardButton(text = 'Product3', callback_data='product_buying')
but_4 = InlineKeyboardButton(text = 'Product4', callback_data='product_buying')
kb_vit.add(but_1, but_2)
kb_vit.add(but_3, but_4)

#initiate_db()

@dp.message_handler(commands=['start'])
async def start_message(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb1)

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:', reply_markup=kb2)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')

@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age_ = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth_=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight_=message.text)
    data = await state.get_data()
    calories = (int(data['weight_'])*10 + 6.25*int(data['growth_']) - 5*int(data['age_']) - 161)
    await message.answer(f'Ваша норма калорий {int(calories)}')
    await state.finish()

@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for i in range(1, 5):
        with open(f'files/{i}.jpg', 'rb') as img:
            await message.answer_photo(img, f'Название: {get_all_products(i)[0]} | Описание: {get_all_products(i)[1]} | Цена: {get_all_products(i)[2]}')
    await message.answer('Выберите продукт для покупки:', reply_markup=kb_vit)

@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')

@dp.message_handler(text='Регистрация')
async def sing_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if is_included(message.text) == False:
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()

@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    add_user(data['username'], data['email'], data['age'])
    await message.answer('Регистрация прошла успешно')
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
