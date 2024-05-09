from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# Inline главная клавиатура с callback
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Каталог', callback_data='catalog')],
    [InlineKeyboardButton(text='Корзина', callback_data='basket'),
     InlineKeyboardButton(text='Контакты', callback_data='contacts')]
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com')]
])

cars = ['Tesla', 'Mercedes', 'BMW', 'Voyah'] # Если каждый раз из базы данных новые значения услуг/вывода запроса и др. (Т.е. динамически меняется список) - мы пользуемся builder

async def inline_cars():
    keybord = InlineKeyboardBuilder() # Можно использовать ReplyKeyboardBuilder
    for car in cars:
        keybord.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/shorts/FpBGy5GL3qQ')) # При ReplyKeyboardBuilder нужно использовать ReplyKeyboardButton
    return keybord.adjust(2).as_markup() # adjust - то сколько кнопок бует в ряду

