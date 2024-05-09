from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Контакты')]
],
    resize_keyboard=True,
    input_field_placeholder='Воспользуйтесь пункт меню')

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://youtube.com')]
])

cars = ['Tesla', 'Mercedes', 'BMW', 'Voyah'] # Если каждый раз из базы данных новые значения услуг/вывода запроса и др. (Т.е. динамически меняется список) - мы пользуемся builder

async def inline_cars():
    keybord = InlineKeyboardBuilder() # Можно использовать ReplyKeyboardBuilder
    for car in cars:
        keybord.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/shorts/FpBGy5GL3qQ')) # При ReplyKeyboardBuilder нужно использовать ReplyKeyboardButton
    return keybord.adjust(2).as_markup() # adjust - то сколько кнопок бует в ряду

