from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class Reg(StatesGroup):
    name = State()
    number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(f'Привет! \nТвой ID: {message.from_user.id}\nИмя: {message.from_user.first_name}' # from_user - хранит всю информацию (first_name, last_name, full_name, является ли premium, может ли вступать в группы, номер телефона при  и т.д.)
                        ,reply_markup=kb.main)
@router.message(Command('help'))
async def get_help(message: Message):
    await message.answer('Это команда /help',
                         reply_markup=kb.settings)

@router.message(F.text == 'Авто')
async def get_auto(message: Message):
    await message.reply('OK!'
                        ,reply_markup=await kb.inline_cars())

@router.message(F.text == 'Как дела?')
async def how_are_you(message: Message):
    await message.answer('OK!')

@router.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIDA2Y8CC6Te9D4rLmITz12H-K0yhUWAAKb1TEb4kzgSRGwEFB0HjnFAQADAgADeQADNQQ' #Также можно указывать и url
                               ,caption='Это сегодняшний прикол с тачкой, мотом и снегом!')

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото {message.photo[-1].file_id}') # [-1] - лучшее качество

@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Вы выбрали каталог', show_alert=True)
    await callback.message.edit_text('Привет!', reply_markup=await kb.inline_cars())

@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state((Reg.name))
    await message.answer('Ведите Ваше имя')

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона') # В идеале сделать клавиатуру, которая будет запрашивать контакт, сейчас полагаемся, что пользователь сам отправит цифры

@router.message(Reg.number
                #,F.contact - как раз на то, чтобы с клавиатуры ловил
                )
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершена. \nИмя: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()